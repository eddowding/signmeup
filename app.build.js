({
    paths: {
        "jquery": "require-jquery"
    },
    findNestedDependencies: true,
    appDir: "client/",
    baseUrl: "js/",
    mainConfigFile: 'client/js/main.js',
    dir: "client-build",
    // out: "main-built.js",
    modules: [
        {
            name: "main",
            exclude: ["jquery"]
        },
    ],
})

