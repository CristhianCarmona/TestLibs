ENV=`python -c "import sys; print sys.prefix"`
PYTHON=`python -c "import sys; print sys.real_prefix"`/bin/python
export PYTHONHOME=$ENV
ENVDEV=`python -c "import sys; import os; home=os.environ['HOME']; sys.path.append(home+'/envdev/TestLibs/lib');print home+'/envdev/TestLibs/lib'"`
export PYTHONPATH=$ENVDEV
compiled=`python -c "import sys; import os; import compileall; home=os.environ['HOME']; sys.path.append(home+'/envdev/TestLibs/lib'); compileall.compile_dir(home+'/envdev/TestLibs/lib', force=True)"`
exec $PYTHON "ride.py"
