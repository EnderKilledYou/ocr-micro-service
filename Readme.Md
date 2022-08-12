## Ocr Python Microservice 

post image as a file to /ocr to get an OCRResult back

thread pooled (set in ocr_producer constructor for how many consumers) and 15 second time out (set in ocr_producer get_one)

you can increase the time out to let it wait forever and queue up tons of images to be processed skipping the upload time as a gap

`gcloud run deploy --source ./`