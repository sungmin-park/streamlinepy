(function() {
    var streamlinepy = require('streamlinepy');
    streamlinepy.modules['test.sleep'] = {
        __name__: 'test.sleep', __file__: 'test/sleep.py', __dict__: {},
        __init__: function (__name__, __file__, _) {
            var sleep = streamlinepy.import_from('sleep', 'time', __file__, _);
            console.info("sleep");
            sleep(1, _);
            console.info("wake up");
        }
    };
    console.info(streamlinepy.modules)
})();
