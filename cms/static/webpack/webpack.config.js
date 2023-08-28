const path = require('path')
const MiniCSSExtractPlugin = require('mini-css-extract-plugin')
const projectPath = path.resolve(__dirname);
console.log(projectPath);

module.exports = {
    mode: 'development',
    entry: {
        cms: ['./src/js/main.js', './src/scss/styles.scss'],
        admin: ['..../admin/static/js/sb-admin-2.js', '..../admin/static/css/sb-admin-2.min.css'],
    },
    output: {
        clean: true,
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '../cms/js')
    },
    module: {
        rules: [
            {
                test: /\.(scss)$/,
                use: [
                    // fallback to style-loader in development
                    process.env.NODE_ENV !== 'production'
                        ? 'style-loader'
                        : MiniCSSExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCSSExtractPlugin({
            filename: '[name].css'
        })
    ],
    watch: true,
}