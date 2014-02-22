var streamlinepy = {};

streamlinepy.sys = {
    modules: {
        time: {
            sleep: function(sec, cb) {
                setTimeout(function(){
                    cb(null);
                }, sec * 1000);
            }
        }
    }
};

streamlinepy.import_ = function(name, __module__, _) {
    var module = null;
    if (__module__) {
        module = streamlinepy.sys.modules[__module__.__name__ + '.' + name];
    }
    if (!module) {
        module = streamlinepy.sys.modules[name];
    }
    if (module.__init__ && !module.__init__.initizlied) {
        module.__init__(module, _);
        module.__init__.initizlied = true;
    }
    return module
};

streamlinepy.import_from = function(obj, from, __module__, _) {
    var module = streamlinepy.import_(from, __module__, _);
    return module[obj];
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = streamlinepy;
}
else {
    window.streamlinepy = streamlinepy;
}