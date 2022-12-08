class SomeThing:

    def run(self):
        print ( "running")
        return self

    
    def sleep(self):
        print ( "sleeping")
        return self


thing_1 = SomeThing()

thing_1.run().sleep()