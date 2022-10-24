#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, model, view):

        self._model = model
        self._view  = view.ui

        self._connectSignalsAndSlots()

        self._file_name = ''
        self._start_new()

    #--------------------------------------------------------------------------#
    def _connectSignalsAndSlots(self):

        # File actions
        self._view.action_New    .triggered.connect( self._new     )
        self._view.action_Open   .triggered.connect( self._open    )
        self._view.action_Save   .triggered.connect( self._save    )
        self._view.action_Save_as.triggered.connect( self._save_as )
        self._view.action_Exit   .triggered.connect( self._exit    )

        # Edit actions
        self._view.action_Undo .triggered.connect( self._undo  )
        self._view.action_Redo .triggered.connect( self._redo  )
        self._view.action_Reset.triggered.connect( self._reset )

        # Game actions
        self._view.action_Run  .triggered.connect( self._run   )
        self._view.action_Build.triggered.connect( self._build )

        # Help actions
        self._view.action_About   .triggered.connect( self._about )
        self._view.action_Contents.triggered.connect( self._help  )

        # Test 
        self._view.pushButton.clicked.connect(self._change_world)

    # Action calls
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def _change_world(self):
        print('Contr: Changing world')
        self._changed = True

    #--------------------------------------------------------------------------#
    def _new(self):
        if self._confirm_deletion():
            self._file_name = ''
            self._start_new()

    #--------------------------------------------------------------------------#
    def _open(self):
        if self._confirm_deletion():
            print('Contr: Get file not yet implemented!')
            self._file_name = 'get_file_name'
            self._model.open( self._file_name )
            self._changed = False
            self._update()

    #--------------------------------------------------------------------------#
    def _save(self):

        if not self._file_name:
            self._save_as()

        elif self._changed:
            self._model.save( self._file_name )
            self._changed = False

    #--------------------------------------------------------------------------#
    def _save_as(self):
        print('Contr: Get file not yet implemented!')
        self._file_name = 'get_file_name'
        self._model.save( self._file_name )
        self._changed = False

    #--------------------------------------------------------------------------#
    def _exit(self):
        if self._confirm_deletion():
            QApplication.quit()

    #--------------------------------------------------------------------------#
    def _undo(self):
        self._model.undo()
        self._update()

        print('Contr: Unchanging world')
        self._changed = False

    #--------------------------------------------------------------------------#
    def _redo(self):
        self._model.redo()
        self._update()

    #--------------------------------------------------------------------------#
    def _reset(self):
        if self._confirm_deletion():
            self._start_new()

    #--------------------------------------------------------------------------#
    def _run(self):
        self._block_ui()
        self._model.run()

    #--------------------------------------------------------------------------#
    def _build(self):
        print('Contr: Get file not yet implemented!')
        self._exe_file_name = 'get_file_name'
        self._block_ui()
        self._model.build( self._exe_file_name )

    #--------------------------------------------------------------------------#
    def _about(self):
        print('Contr: About not yet implemented!')

    #--------------------------------------------------------------------------#
    def _help(self):
        print('Contr: Help contents not yet implemented!')

    # Internal tools
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def _start_new(self):
        self._model.new()
        self._changed = False
        self._update()

    #--------------------------------------------------------------------------#
    def _confirm_deletion(self):

        if self._changed:
            print('Contr: Confirm deletion not yet implemented!')
            return False

        return True

    #--------------------------------------------------------------------------#
    def _block_ui(self):
        print('Contr: Block not yet implemented!')

    #--------------------------------------------------------------------------#
    def _update(self):
        print('Contr: Update not yet implemented!')

#------------------------------------------------------------------------------#
