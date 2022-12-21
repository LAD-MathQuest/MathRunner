#------------------------------------------------------------------------------#

from PySide6.QtWidgets import ( QApplication, 
                                QFileDialog, 
                                QMessageBox )

import parameters as par

from ui.main_model import MainModel

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.model = MainModel()
        self.win   = window
        self.ui    = window.ui

        self.last_dir  = str(par.HOME)
        self.file_name = ''
        self.start_new()

        self.connect_signals_and_slots()

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
    def new(self):

        if self.confirm_deletion():
            self.file_name = ''
            self.start_new()

    #--------------------------------------------------------------------------#
    def open(self):

        if self.confirm_deletion():

            path  = par.RESOURCES / 'games' 
            fname = self.get_open_fname('Chose a game description', path, 'game' )

            if fname:
                # TODO try:
                self.file_name = fname
                self.model.open(self.file_name)
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
        self.exe_file_name = 'get_file_name'
        self.block_ui()
        self.model.build( self.exe_file_name )

    #--------------------------------------------------------------------------#
    def about(self):
        QMessageBox.about(self.win, par.TITLE+' - About', par.ABOUT )

    #--------------------------------------------------------------------------#
    def help(self):
        QMessageBox.about(self.win, par.TITLE+' - Help', par.ABOUT )

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
            return False

        return True

    #--------------------------------------------------------------------------#
    def block_ui(self):
        pass

    #--------------------------------------------------------------------------#
    def update(self):

        meta = self.model.meta
        
        self.ui.lineEdit_GameName.setText(meta.soft_name)
        self.ui.lineEdit_Author  .setText(meta.soft_author)

        self.ui.plainTextEdit_GameDescription.setPlainText(meta.soft_description)

    #-------------------------------------------------------------------------#
    def error_box( self, title, message ):
        QMessageBox.critical( self.win, title, message,
                              buttons=QMessageBox.StandardButton.Ok )

    #--------------------------------------------------------------------------#
    def get_open_fname( self, title, path, ext ):
        fname, _ = QFileDialog.getOpenFileName( parent  = self.win, 
                                                caption = title, 
                                                dir     = str(path),
                                                filter  = '*.' + ext )
        return fname
    
    #--------------------------------------------------------------------------#
    def get_save_fname( self, title, ext, suggestion = '' ):

        if not suggestion:
            suggestion = self.last_dir

        fname, _ = QFileDialog.getSaveFileName( parent  = self.win, 
                                                caption = title, 
                                                dir     = suggestion, 
                                                filter  = '*.' + ext )
        if fname:
            ee = '.' + ext
            nn = len(ee)
            if len(fname) < nn or fname[-nn:] != ee:
                fname += ee
    
        return fname

#------------------------------------------------------------------------------#
