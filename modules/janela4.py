import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1UXmHaGxqdgw_COZeQPKyAUvLjS4nYVOi2hIDCJmr31s'
RANGE_NAME = 'Página1!A2:G'

class Janela4(Screen):

    def on_pre_enter(self):
        #Connect Google Sheets
        self.connect_google()

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60), self.sort_on_signal),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30), self.sort_on_schedule),
                ("Team Lead", dp(30), self.sort_on_team),
            ],
            row_data= self.dados  #[
            #     (
            #         "1",
            #         ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
            #         "Astrid: NE shared managed",
            #         "Medium",
            #         "Triaged",
            #         "0:33",
            #         "Chase Nguyen",
            #     ),
            #     (
            #         "2",
            #         ("alert-circle", [1, 0, 0, 1], "Offline"),
            #         "Cosmo: prod shared ares",
            #         "Huge",
            #         "Triaged",
            #         "0:39",
            #         "Brie Furman",
            #     ),
            #     (
            #         "3",
            #         (
            #             "checkbox-marked-circle",
            #             [39 / 256, 174 / 256, 96 / 256, 1],
            #             "Online",
            #         ),
            #         "Phoenix: prod shared lyra-lists",
            #         "Minor",
            #         "Not Triaged",
            #         "3:12",
            #         "Jeremy lake",
            #     ),
            #     (
            #         "4",
            #         (
            #             "checkbox-marked-circle",
            #             [39 / 256, 174 / 256, 96 / 256, 1],
            #             "Online",
            #         ),
            #         "Sirius: NW prod shared locations",
            #         "Negligible",
            #         "Triaged",
            #         "13:18",
            #         "Angelica Howards",
            #     ),
            #     (
            #         "5",
            #         (
            #             "checkbox-marked-circle",
            #             [39 / 256, 174 / 256, 96 / 256, 1],
            #             "Online",
            #         ),
            #         "Sirius: prod independent account",
            #         "Negligible",
            #         "Triaged",
            #         "22:06",
            #         "Diane Okuma",
            #     ),
            # ],
        ,
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        screen = MDScreen()
        self.ids.box.add_widget(self.data_tables)



    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''



        # Sorting Methods:
        # since the https://github.com/kivymd/KivyMD/pull/914 request, the
        # sorting method requires you to sort out the indexes of each data value
        # for the support of selections.
        #
        # The most common method to do this is with the use of the builtin function
        # zip and enumerate, see the example below for more info.
        #
        # The result given by these funcitons must be a list in the format of
        # [Indexes, Sorted_Row_Data]

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))

    def connect_google(self):
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                        range=RANGE_NAME).execute()
            wks_values = result.get('values', [])

            if not wks_values:
                print('No data found.')
                return
            else:
                self.dados = []
                status = {'No Signal': ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                          'Offline': ("alert-circle", [1, 0, 0, 1], "Offline"),
                          'Online': ("checkbox-marked-circle", [39 / 256, 174 / 256, 96 / 256, 1], "Online")}

            print('Name, Major:')
            for row in wks_values:

                dados_interm = []
                for idx, v in enumerate(row):

                    if idx == 1:

                        dados_interm.append(status[v])

                    else:
                        dados_interm.append(v)


                self.dados.append(tuple(dados_interm))
                print(self.dados)

        except HttpError as err:
            print(err)
