class OcrResult:
    success: bool = False
    error_message: str = ""
    text: str = ""

    def __init__(self,**kwargs):
        for key in kwargs:
            setattr(self,key,kwargs[key])

    def to_dict(self):
        return {
            'success': self.success,
            'error_message': self.error_message,
            'text': self.text
        }
