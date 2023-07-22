import pandas as pd
import qrcode

file = pd.read_csv("file.csv")

lst = []

for index, values in file.iterrows():
    name = values["Name"]
    username = values["Username"]
    email = values["Email"]

    data = f'''Name: {name}
            Username: {username}
            Email: {email}
            '''
     
    QRCodefile = f"num_{index}.png"

    # Generating the QR code
    QRimage = qrcode.make(data)

    # Saving image into a file
    QRimage.save(QRCodefile)
    lstdata = f"num_{index}"
    lst.append(lstdata)

print(lst)
file.insert(2, "QR", lst) 

print(file.head())
file.to_csv("newfile.csv", index = False ,header = True)


    
