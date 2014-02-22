u = require 'underscore'
child_process = require('child_process')

class ImportError extends Error

py = module.exports =
  modules:
    time:
      sleep: (sec, cb) ->
        setTimeout(
          ->
            cb null
        , sec * 1000
        )

py.import = (moduleName, fileName, __name__, _) ->
  console.info py.modules
  module = py.modules[moduleName]
  if not module
    throw new ImportError "No module named #{moduleName}"
  if module.__init__?.initialized
    mdoule.__init__ __name__ ? moduleName, fileName, _
    module.__init__.initialized = true
  module

py.import_from = (objName, moduleName, fileName, _) ->
  py.import(moduleName, fileName, null, _)

exec = (cmd, cb) ->
  child_process.exec cmd, (err, stdout, stderr) ->
    cb err, stdout: stdout, stderr: stderr

run = (source, _) ->
  {stdout, stderr} = exec "python streamline #{source}", _
  if stderr
    throw stderr
  fs = require('fs')
  fs.writeFile source[...-3] + '._js', stdout, _
  console.info "./#{source[...-3]}"
  require "./#{source[...-3]}"
  py.modules
  py.import 'test.sleep', '', '__main__', _

if require.main is module
  #noinspection JSUnresolvedVariable
  source = u.last process.argv
  run source, (err) ->
    throw err if err
