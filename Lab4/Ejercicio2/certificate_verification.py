import os


def execute():
    # Before starting, we must save this two certificates from wireshark
    #   - The first one, which comes from www.fib.upc.edu (certificadoFIB.cer)
    #   - The second one, which comes from the CA (certificado_GEANT_OV_RSA_CA.pem)
    # Both can be obtained via saving the certificate bytes as raw bytes(we've picked the first two certificates shown
    # in the lsit)

    os.system("openssl x509 -inform DER -in certificadoFIB.cer -out certificadoFIB.pem")
    os.system("openssl ocsp -issuer certificado_GEANT_OV_RSA_CA.pem -cert certificadoFIB.pem "
              "-url http://GEANT.ocsp.sectigo.com -text > verificacion.txt")

    # After that, we open the file and obtain the information
    verification = open("verificacion.txt", "r")
    verificationInfo = verification.read()

    successfulResponse = "OCSP Response Status: successful (0x0)"
    validCertificate = "certificadoFIB.pem: good"
    if successfulResponse in verificationInfo and validCertificate in verificationInfo:
        print(verificationInfo)
        print("Successful verification! " + successfulResponse)
    else:
        print("Something went wrong with the verification")

    verification.close()
    return


# Main
if __name__ == "__main__":
    execute()
