from ipywidgets import *
import ipygee as ui
from .calendar import Calendar


class Scores(ui.widgets.CheckAccordion):
    def __init__(self, **kwargs):
        self.outliers = SelectMultiple(description='Outliers bands')
        self.medoid = SelectMultiple(description='Medoid bands')
        self.doy = Calendar(month=1, day=15)
        self.satellite = Text(description='ratio', value='0.05')
        self.cloud_distance = VBox([
            Text(description='Max distance', value='600'),
            Text(description='Min distance', value='0')
        ])
        self.maskcover = Checkbox(
            value = False,
            description = 'Kernel'
        )
        self.index = SelectMultiple(
            options = ['ndvi', 'nbr'],
            description = 'Bands for index'
        )
        self.multiyear = MultiYear()

        widgets = [self.doy, self.satellite, self.cloud_distance,
                   self.maskcover, self.index, self.outliers, self.medoid,
                   self.multiyear]

        super(Scores, self).__init__(widgets, **kwargs)

        self.set_titles(['DOY', 'Satellite', 'Cloud Distance',
                         'Mask Cover', 'Index', 'Outliers', 'Medoid',
                         'Multi Year'])


class MultiYear(VBox):
    def __init__(self, **kwargs):
        super(MultiYear, self).__init__(**kwargs)
        self.main_year = Select(description='Main year')
        self.ratio = Text(description='ratio', value='0.05')
        self.children = [self.main_year, self.ratio]