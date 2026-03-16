class DialogService:
    
    def __init__(self):
        pass

    def handle_dialog(self, dialog):
        print(f"Dialog message: {dialog.message}")
        dialog.accept()