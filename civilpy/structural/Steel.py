import pandas as pd
import pint
import os
from pathlib import Path

content_root = os.getcwd()
units = pint.UnitRegistry()

def  start():
    temp_var = input('Enter the Section you want to lookup: ')
    steel_member(temp_var)

class steel_member(object):
    """ Class object for a steel structural member

    Allows storage of important variables in a single location
    """
    def __init__(
            self, label=None,
            ref_file=Path(Path(content_root).parent.parent / 'civilpy/data/steel_sections.csv'),
            ref_schema=Path(Path(content_root).parent.parent / 'civilpy/data/steel_schema.csv')
    ):
        self.label = label.upper()
        self.data_path = ref_file
        self.schema_path = ref_schema
        self.properties = {
            'W': None,
            'A': None,
            'd1': None,
            'bf': None,
            'tw': None,
            'tf': None,
            'Ix': None,
            'Zx': None,
            'Sx': None,
            'rx': None,
            'ry': None,
            'J': None
        }

        self.get_data()

    def get_data(self):
        steel_df = pd.read_csv(self.data_path)
        section_filter = steel_df['EDI_Name'] == self.label

        self.properties['W'] = steel_df.loc[section_filter]['W'].item() * \
            (units.lbs / units.foot)
        self.properties['A'] = steel_df.loc[section_filter]['A'].item() * \
            (units.inch ** 2)
        self.properties['d1'] = steel_df.loc[section_filter]['d1'].item() * \
            units.inch
        self.properties['bf'] = steel_df.loc[section_filter]['bf'].item() * \
            units.inch
        self.properties['tw'] = steel_df.loc[section_filter]['tw'].item() * \
            units.inch
        self.properties['tf'] = steel_df.loc[section_filter]['tf'].item() * \
            units.inch
        self.properties['Ix'] = steel_df.loc[section_filter]['Ix'].item() * \
            (units.inch ** 4)
        self.properties['Zx'] = steel_df.loc[section_filter]['Zx'].item() * \
            (units.inch ** 3)
        self.properties['Sx'] = steel_df.loc[section_filter]['Sx'].item() * \
            (units.inch ** 3)
        self.properties['rx'] = steel_df.loc[section_filter]['rx'].item() * \
            units.inch
        self.properties['ry'] = steel_df.loc[section_filter]['ry'].item() * \
            units.inch
        self.properties['J'] = steel_df.loc[section_filter]['J'].item() * \
            (units.inch ** 4)


rebar_table = {  # Bar Number, Weight, Nominal Dia, Nominal Area - BDM 304-6
    '2': {'weight': '0.166', 'dia': '0.25', 'area': '0.05'},
    '3': {'weight': '0.376', 'dia': '0.375', 'area': '0.11'},
    '4': {'weight': '0.668', 'dia': '0.5', 'area': '0.2'},
    '5': {'weight': '1.043', 'dia': '0.625', 'area': '0.31'},
    '6': {'weight': '1.502', 'dia': '0.75', 'area': '0.44'},
    '7': {'weight': '2.044', 'dia': '0.875', 'area': '0.6'},
    '8': {'weight': '2.67', 'dia': '1', 'area': '0.79'},
    '9': {'weight': '3.4', 'dia': '1.128', 'area': '1'},
    '10': {'weight': '4.303', 'dia': '1.27', 'area': '1.27'},
    '11': {'weight': '5.313', 'dia': '1.41', 'area': '1.56'},
    '14': {'weight': '7.65', 'dia': '1.693', 'area': '2.25'},
    '18': {'weight': '13.6', 'dia': '2.257', 'area': '4'},
}
