rlwrap ${WAS_HOME}/bin/wsadmin.sh -lang jython -javaoption -Dcom.ibm.ws.scripting.exceptionPropagation=thrown -javaoption -Dpython.path=${WDR_HOME}/lib/legacy:${WDR_HOME}/lib/common:. -profile ${WDR_HOME}/profile.py
