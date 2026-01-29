import spade
class DummyAgent(spade.agent.Agent):
    async def setup(self):
        print("My first agent")
        print("Hello World! I'm agent {}".format(str(self.jid)))

async def main():
    dummy = DummyAgent("agent-test@xmpp.jp", "abigail111")
    await dummy.start()

if __name__ == "__main__":
    spade.run(main())
