"""
stubs: 
registerCallable(signalID, callable)
unregisterCallable(signalID, callable)
signal(signalID)

signalID: type int
callable: type callable (func, method, class etc.)

Implement the above functions for a publish subscribe system that will register 
callable to a service, unregister callable to a service and singal (or call) 
those callables. 

Assume that your implementation will be used by others for a variety of uses. 
"""