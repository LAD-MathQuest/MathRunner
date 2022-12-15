#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication
from ui.main_model     import MainModel

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.model = MainModel()
        self.win   = window
        self.ui    = window.ui

        self.connect_signals_and_slots()

        self.file_name = ''
        self.start_new()

    #--------------------------------------------------------------------------#
    def connect_signals_and_slots(self):

        # File actions
        self.ui.action_New    .triggered.connect( self.new     )
        self.ui.action_Open   .triggered.connect( self.open    )
        self.ui.action_Save   .triggered.connect( self.save    )
        self.ui.action_Save_as.triggered.connect( self.save_as )
        self.ui.action_Exit   .triggered.connect( self.exit    )

        # Edit actions
        self.ui.action_Undo .triggered.connect( self.undo  )
        self.ui.action_Redo .triggered.connect( self.redo  )
        self.ui.action_Reset.triggered.connect( self.reset )

        # Game actions
        self.ui.action_Run  .triggered.connect( self.run   )
        self.ui.action_Build.triggered.connect( self.build )

        # Help actions
        self.ui.action_About   .triggered.connect( self.about )
        self.ui.action_Contents.triggered.connect( self.help  )

    # Action calls
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def change_world(self):
        print('Contr: Changing world')
        self.changed = True

    #--------------------------------------------------------------------------#
    def new(self):
        if self.confirm_deletion():
            self.file_name = ''
            self.start_new()

    #--------------------------------------------------------------------------#
    def open(self):
        if self.confirm_deletion():
            print('Contr: Get file not yet implemented!')
            self.file_name = 'get_file_name'
            self.model.open( self.file_name )
            self.changed = False
            self.update()

    #--------------------------------------------------------------------------#
    def save(self):

        if not self.file_name:
            self.save_as()

        elif self.changed:
            self.model.save( self.file_name )
            self.changed = False

    #--------------------------------------------------------------------------#
    def save_as(self):
        print('Contr: Get file not yet implemented!')
        self.file_name = 'get_file_name'
        self.model.save( self.file_name )
        self.changed = False

    #--------------------------------------------------------------------------#
    def exit(self):
        if self.confirm_deletion():
            QApplication.quit()

    #--------------------------------------------------------------------------#
    def undo(self):
        self.model.undo()
        self.update()

        print('Contr: Unchanging world')
        self.changed = False

    #--------------------------------------------------------------------------#
    def redo(self):
        self.model.redo()
        self.update()

    #--------------------------------------------------------------------------#
    def reset(self):
        if self.confirm_deletion():
            self.start_new()

    #--------------------------------------------------------------------------#
    def run(self):
        self.block_ui()
        self.model.run()

    #--------------------------------------------------------------------------#
    def build(self):
        print('Contr: Get file not yet implemented!')
        self.exe_file_name = 'get_file_name'
        self.block_ui()
        self.model.build( self.exe_file_name )

    #--------------------------------------------------------------------------#
    def about(self):
        print('Contr: About not yet implemented!')

    #--------------------------------------------------------------------------#
    def help(self):
        print('Contr: Help contents not yet implemented!')

    # Internal tools
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def start_new(self):
        self.model.new()
        self.changed = False
        self.update()

    #--------------------------------------------------------------------------#
    def confirm_deletion(self):

        if self.changed:
            print('Contr: Confirm deletion not yet implemented!')
            return False

        return True

    #--------------------------------------------------------------------------#
    def block_ui(self):
        print('Contr: Block not yet implemented!')

    #--------------------------------------------------------------------------#
    def update(self):
        print('Contr: Update not yet implemented!')

#------------------------------------------------------------------------------#
