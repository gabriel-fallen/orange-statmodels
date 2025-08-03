from Orange.data import Table, table_to_frame
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg

import statsmodels.api as sm
from patsy import dmatrices


class OLSWidget(OWWidget):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = "Ordinary Least Squares"
    description = "Fits a model specified via a formula to the data provided."
    icon = "icons/UnivariateRegression.svg"
    priority = 100  # where in the widget order it will appear
    keywords = ["widget", "data"]
    want_main_area = False
    resizing_enabled = True

    formula = Setting("")

    class Inputs:
        # specify the name of the input and the type
        data = Input("Data", Table)

    # class Outputs:
        # if there are two or more outputs, default=True marks the default output
        # data = Output("Data", Table, default=True)

    # same class can be initiated for Error and Information messages
    class Warning(OWWidget.Warning):
        no_data = Msg("No input data")
        no_formula = Msg("No formula is provided")

    def __init__(self):
        super().__init__()
        self.data : Table | None = None

        self.formula_box = gui.lineEdit(
            self.controlArea, self, "formula", box="Formula", callback=self.commit)
        self.info_box = gui.widgetLabel(self.controlArea, '')

    @Inputs.data
    def set_data(self, data):
        if data:
            self.data = data
            self.try_fit()
        else:
            self.data = None

    def commit(self):
        # self.Outputs.data.send(self.data)
        self.try_fit()

    def try_fit(self):
        self.Warning.no_data(shown=not self.data)
        self.Warning.no_formula(shown=not self.formula)
        if not self.data or not self.formula: return

        try:
            y, X = dmatrices(self.formula, data=table_to_frame(self.data), return_type='dataframe')
            res = sm.OLS(y, X).fit()
            self.info_box.setText(str(res.summary()))
        except Exception as ex:
            self.info_box.setText(str(ex))

    def send_report(self):
        # self.report_plot() includes visualizations in the report
        self.report_caption(self.formula)


if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview  # since Orange 3.20.0
    WidgetPreview(OLSWidget).run()
