var streamlinepy;
if (typeof require !== 'undefined') {
    streamlinepy = require('streamlinepy');
}
else {
    streamlinepy = window.streamlinepy;
}

streamlinepy.sys.modules['sleep'] = {
    __name__: 'sleep', __file__: 'sleep.py',
    __init__: (function (__module__, _) {
        var sleep = streamlinepy.import_from('sleep', 'time', __module__, _);
        console.info('sleep');
        sleep(1, _);
        console.info('wake up');
    })
};

