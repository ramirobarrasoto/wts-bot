const {Client, LocalAuth} = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client({authStrategy: new LocalAuth()});

//Mostrar el qr en consola 
client.on('qr', (qr)=> {qrcode.generate(qr, {small: true})});

//confirmar que está listo
client.on('ready', ()=>{console.log('Bot conectado y listo')});

// Lógica de respuesta

client.on('message', async (message)=>{if (message.body.toLowerCase()=== '@bot reportar')
    await message.reply('¿Qué tipo de reporte querés realizar?\n1. Problema técnico\n2. Ausencia\n3. Otro\n(Responde con el número de la opción')
});

client.initialize();