
const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        ruta_bundle: ['./static/js/ruta_main.js'],
        main_bundle: ['bootstrap/dist/js/bootstrap.bundle.min.js']
    },
    output: {
        path: path.resolve(__dirname, 'static/js/'),
    },
    module: {
        rules: [
          {
            test: require.resolve("jquery"),
            loader: "expose-loader",
            options: {
                exposes: ["$", "jQuery"],
            },
          }
        ]
      },
    target: 'web',
    mode: 'production',
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery", 
            jQuery: "jquery", 
            jquery: "jquery"
        }),
    ]
};