driver = require('bigchaindb-driver')
const lineByLine = require('n-readlines');
const API_PATH = 'http://localhost:9984/api/v1/'
const conn = new driver.Connection(API_PATH)
const fs = require('fs')


const liner = new lineByLine('details.txt');
let line;
var i=0;
const ar=[]
while (line = liner.next()) {
    ar[i]=line;
    i++;
}

var keys;
try 
{
  keys = fs.readFileSync('hash.txt', 'utf8')
} 
catch (err){}

const citizen = new driver.Ed25519Keypair()


const assetdata = {
    'Case': {
            'Aadhaar':keys.toString(),
            'Action': 'Filing Case ing blockchain',
            'Location':ar[1].toString(),
            'Category':ar[2].toString(),
            'Detailed Description':ar[3].toString(),
             
            'Public key' : citizen.publicKey,
            'Time' :new Date().toLocaleString(),
    }
}
const metadata = {'Election': 'ongoing'}
const txCreateAliceSimple = driver.Transaction.makeCreateTransaction(
    assetdata,
    metadata,
    [ driver.Transaction.makeOutput(
            driver.Transaction.makeEd25519Condition(citizen.publicKey))
    ],
    citizen.publicKey
)
const txCreateAliceSimpleSigned = driver.Transaction.signTransaction(txCreateAliceSimple, citizen.privateKey)
conn.postTransactionCommit(txCreateAliceSimpleSigned)
txid = txCreateAliceSimpleSigned.id
