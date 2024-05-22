import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the versiom of the QR code  high the number  bigger  the code image and compatible pictuers
    box_size = 10, # size  of the box where  qr code will be display 
    border = 5, #  it is the white  part of image -----border in all 4 slides
    
)

data = "url of the website if one has one"
#if  yoou dont want to redirect  and  create for normal  text  that write  text in quotes 


qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black" ,back_color = "white")
img.save("test.png")

