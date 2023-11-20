from hashlib import sha256
from BlockChainRSA import *
import pickle

VALID_BLOCK_LIMIT = 42


def writeBlockInfo(f_output, block, nBlock, transaction_signature):
    f_output.write("Block # " + str(nBlock) + '\n')
    f_output.write("Previous block hash: " + str(block.previous_block_hash) + '\n')
    f_output.write("Block hash: " + str(block.block_hash) + '\n')
    f_output.write("Block seed: " + str(block.seed) + '\n')
    f_output.write("Transaction signature: " + str(transaction_signature) + '\n')
    f_output.write("Block verification returned: " + str(block.verify_block()) + '\n')
    f_output.write("--------------------------------------------------------------------------\n")


def force_wrong_block(bc, transaction):
    b = bc.list_of_blocks[-1]
    new_block = block()
    new_block.previous_block_hash = b.previous_block_hash
    new_block.transaction = transaction
    new_block.generate_hash(False)  # Generamos un hash NO válido
    bc.list_of_blocks.append(new_block)


def generate_blockchain(filename, nBlocks, usingPickle, force_wrong_hash):
    RSAKey = rsa_key()
    if not usingPickle:
        f = open(filename + ".txt", "w")
        f.write("--------------------------------------------------------------------------\n")
    transactions = []
    transactions.append(transaction(int(sha256(f"Transacción número {0}".encode()).hexdigest(), 16), RSAKey))
    bc = block_chain(transactions[0])
    if not usingPickle:
        writeBlockInfo(f, bc.list_of_blocks[0], 0, transactions[0].signature)
    for i in range(1, nBlocks):
        transactions.append(transaction(int(sha256(f"Transacción número {0}".encode()).hexdigest(), 16), RSAKey))
        if force_wrong_hash and i == VALID_BLOCK_LIMIT:
            force_wrong_block(bc, transactions[i])
        else:
            bc.add_block(transactions[i])

        if not usingPickle:
            writeBlockInfo(f, bc.list_of_blocks[i], i, transactions[i].signature)

    if not usingPickle:
        f.close()
    else:
        with open(filename + ".pickle", "wb") as file:
            pickle.dump(bc, file)


if __name__ == "__main__":
    generate_blockchain("./100BlockChain", 100, True, False)
    generate_blockchain("./100BlockChain", 100, False, False)
    generate_blockchain("./100BlockChainUntil42", 100, True, True)
    generate_blockchain("./100BlockChainUntil42", 100, False, True)
