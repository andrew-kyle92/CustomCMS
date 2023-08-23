const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: {
    'js/main': './src/js/main.js',
    'css/style': './src/sass/style.scss',
  },
  performance: {
    hints: false,
    maxEntrypointSize: 512000,
    maxAssetSize: 512000
  },
  devtool: 'source-map',
  mode: 'production',
  module: { 
    rules: [
      {
        test: /\.(s(a|c)ss)$/,
        use: [
          MiniCssExtractPlugin.loader, 
          {
            loader: 'css-loader', 
            options: {
              url: false,
              sourceMap: true, 
            }
          },
          {
            loader: 'postcss-loader', 
            options: {
              sourceMap: true,
              postcssOptions: {
                plugins: [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader', 
            options: {
              sourceMap: true,
            }
          },
        ]
      }, 
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
    ]
  },
  plugins: [
    new MiniCssExtractPlugin(),
    new CopyPlugin({
      patterns: [
        { from: "node_modules/bootstrap/dist/js/bootstrap.min.js", to: "js/vendor" },
        { from: "node_modules/bootstrap/dist/js/bootstrap.min.js.map", to: "js/vendor" },        
        { from: "node_modules/@popperjs/core/dist/umd/popper.min.js", to: "js/vendor" },
        { from: "node_modules/@popperjs/core/dist/umd/popper.min.js.map", to: "js/vendor" },
      ],
    }),
  ],
  output: {
    clean: true,
    path: path.resolve(__dirname, '../'),
  },
  watch: true,
}; 