const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = {
    entry: {
        main: './app/js/app.jsx',
        vendor1: [
            'react',
            'redux',
            'core-js',
            'react-dom',
            'react-redux',
            'redux-thunk',
            'react-router',
            'react-router-dom',
            'connected-react-router',
        ],
        vendor2: [
            'graphql',
            'react-apollo',
            'apollo-client',
        ],
    },
    output: {
        path: path.join(__dirname, 'dist', 'assets'),
        filename: '[name].[chunkhash].js',
        publicPath: '/assets/',
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        modules: [
            path.resolve('./app'),
            path.resolve('./app/js'),
            'node_modules',
        ],
    },
    plugins: [
        new webpack.NamedChunksPlugin(),
        new webpack.DefinePlugin({
            process: {
                env: {
                    NODE_ENV: JSON.stringify('production'),
                    GRAPGQL_ROOT: JSON.stringify(process.env.GRAPGQL_ROOT || '/graphql'),
                },
            },
        }),
        new webpack.optimize.CommonsChunkPlugin({ name: ['vendor1', 'vendor2'], minChunks: Infinity }),
        new webpack.optimize.CommonsChunkPlugin({ name: 'main', async: true, minChunks: 2 }),
        new webpack.optimize.MinChunkSizePlugin({ minChunkSize: 8192 }),
        new webpack.optimize.CommonsChunkPlugin({ name: 'runtime' }),
        new HtmlWebpackPlugin({
            chunksSortMode: 'dependency',
            title: 'Arena Helper',
            filename: '../index.html',
            template: './app/index.ejs',
        }),
        new webpack.optimize.UglifyJsPlugin({
            parallel: true,
            sourceMap: false,
            compress: {
                warnings: false,
            },
            output: {
                comments: false,
            },
        }),
        new ExtractTextPlugin({
            filename: '[name].[chunkhash].css',
            allChunks: true,
        }),
        ...process.env.DEBUG ? [new BundleAnalyzerPlugin({
                analyzerMode: 'server',
            })] : [],
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
                loader: ExtractTextPlugin.extract(['css-loader', 'resolve-url-loader', 'sass-loader']),
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
