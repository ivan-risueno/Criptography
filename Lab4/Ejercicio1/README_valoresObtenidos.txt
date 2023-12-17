A continuación se muestran los paquetes desplegados hasta llegar a los datos obtenidos(clave pública Q y firma f):

Paquete Certificate, Certificate Verify, Finished:
  Transport Layer Security:	# (1/2)	
    TLSv1.3 Record Layer: Handshake Protocol: Certificate:
      Handshake Protocol: Certificate:
        Certificates (3508 bytes):	# Cogemos el primer certificado, que corresponde al de wikipedia
          Certificate: 3082084...
            signedCertificate:
              subjectPublicKeyInfo:
                subjectPublicKey: 043561f4211aff6ac43bfa0647c6196ebe7038f1dc16b1bc381412d4142b1c0b318159f567f6e72ad13c1efaaea7ed065dd66f5d894c6bc8b0e00f83cff5d38ada

Qx: 0x3561f4211aff6ac43bfa0647c6196ebe7038f1dc16b1bc381412d4142b1c0b31
Qy: 0x8159f567f6e72ad13c1efaaea7ed065dd66f5d894c6bc8b0e00f83cff5d38ada

Paquete Certificate, Certificate Verify, Finished:
  Transport Layer Security:	# (2/2)
    TLSv1.3 Record Layer: Handshake Protocol: Certificate Verify:
      Handshake Protocol: Certificate Verify:
        Signature Algorithm: ecdsa_secp256r1_sha256 (0x0403):
         Signature: 3046022100a3eb0caf2ac3852d527034db8493ea2418c2c62a32606229f82d22c2e68db13a022100f4e1203fff6a2cf02c4e65ccee949e3f01e705c0c616d86dae579135a8ec7f33

f1: 0x00a3eb0caf2ac3852d527034db8493ea2418c2c62a32606229f82d22c2e68db13a
f2: 0x00f4e1203fff6a2cf02c4e65ccee949e3f01e705c0c616d86dae579135a8ec7f33
