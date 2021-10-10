
const path = require('path');

module.exports = {
    entry: ['./static/js/ruta_main.js'],
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static/js/'),
    },
    target: 'web',
    mode: 'production',
};