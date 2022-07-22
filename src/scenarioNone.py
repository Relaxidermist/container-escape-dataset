import command_line
import random


class ScenarioNone:
    """
    ScenarioNone
    """

    def __init__(self):
        self._name = 'none'
        self._annotationFile = None # Set later in init

    def getName(self):
        """
        Gets the name of the scenario.
        """
        return self._name

    def init(self, scheduler, experimentSeconds, annotationFile):
        """
        Setup any resources for the scenario.
        Logging is not active.
        """
        self._annotationFile = annotationFile

        # Start the container for unauthorized executing shell on host.
        #self.execute( 'docker run -d=true --name=ESCAPE_A --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu_shell_dos bash' )

        # Schedule the escape/attack
        #attackSecond = random.randint(1, experimentSeconds)
        print( 'SCENARIO ' + self._name + ': No attack scheduled.' )
        #scheduler.enter( attackSecond, 1, self.onEvent )


    def start(self):
        """
        May be called multiple times during experiment.
        Logging is active.
        """

    def onEvent(self):
        """
        Event occurred.  For example execute a series of
        commands to carry out an attack.
        """
        pass

    def stop(self):
        """
        May be called multiple times during experiment.
        Logging is active.
        """

    def destroy(self):
        """
        Tears down the scenario, for example, stop container.
        Logging is not active
        """
        pass

    def execute( self, command ):
        """
        Convenience to call execute and print out results.
        """
        result = command_line.execute( command )
        for line in result:
            print( 'Scenario ' + self._name + ': ' + line)
