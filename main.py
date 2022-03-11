import  qrcode
import  image

qr = qrcode.QRCode(
    version=15, # 15 means the version of qr code high the number bigger the code image and complicated picture
    box_size=3, #size of box where qr code will be display
    border= 3, # it is the white part of image --border in on four side with white colour

)
data = "https://github.com/GaneshKutwal"
# as a have given the both of the path of youtube video
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(file ="orange",back_color = "white")
img.save("Test.png")




