module.exports = {
    devServer: {
        port: 8080, // This is the port where your Vue.js app will run
        proxy: {
            '/pins': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
                pathRewrite: { '^/pins': '/pins' },
            },
        },
    },
};