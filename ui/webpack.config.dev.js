const autoprefixer = require('autoprefixer');
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const eslintFormatter = require('react-dev-utils/eslintFormatter');

module.exports = {
    entry: [
        'react-hot-loader/patch',
        'webpack-dev-server/client?http://localhost:5000',
        'webpack/hot/only-dev-server',
        './app/js/app.jsx',
    ],
    output: {
        path: __dirname,
        filename: '[name].bundle.js',
        publicPath: '/',
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        modules: [
            path.resolve('./app'),
            path.resolve('./app/js'),
            'node_modules',
        ],
    },
    devtool: 'source-map',
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NamedModulesPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.DefinePlugin({
            process: {
                env: {
                    NODE_ENV: JSON.stringify('development'),
                    GRAPGQL_ROOT: JSON.stringify(process.env.GRAPGQL_ROOT || '/graphql'),
                },
            },
        }),
        new HtmlWebpackPlugin({
            title: 'Arena Helper',
            template: './app/index.ejs',
        }),
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loaders: ['babel-loader'],
                exclude: /node_modules/,
            },
            {
                test: /\.(graphql|gql)$/,
                exclude: /node_modules/,
                loaders: ['graphql-tag/loader'],
            },
            {
                test: /\.s?css$/,
                loaders: ['style-loader', 'css-loader', 'resolve-url-loader', 'sass-loader'],
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'url-loader?limit=10000&mimetype=application/font-woff',
            },
            {
                test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'file-loader',
            },
            {
                test: /\.(gif|png|jpg|jpeg)(\?[a-z0-9]+)?$/,
                loader: 'url-loader?limit=8192',
            },
        ],
    },
};