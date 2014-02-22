(function() {
    var streamlinepy = require('streamlinepy');
    streamlinepy.modules['{{name}}'] = {
        __name__: '{{ name }}', __file__: '{{ filename }}', __dict__: {},
        __init__: function (__name__, __file__, _) {
            {{ stmts|indent(12) }}
        }
    };
    console.info(streamlinepy.modules)
})();
