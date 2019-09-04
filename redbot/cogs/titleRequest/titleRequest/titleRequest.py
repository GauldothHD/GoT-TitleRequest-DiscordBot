from redbot.core import commands

class TitleRequest(commands.Cog):
    """My custom cog"""
    gmHeader = "GM line: "
    gmMessage = ""

    listGmUser = []
    builderLine = ""

    def addLineGM(self, user):
        if user in self.listGmUser:
            raise Exception("user already in line")            
        else:
            self.listGmUser.append(user)          

    def removeLineGM(self, user):
        if user in self.listGmUser:
            self.listGmUser.remove(user)            
        else:
            raise Exception("user not in line")
             

    def buildGmLineMessage(self):
        LineMessage = ""
        for user in self.listGmUser:
            LineMessage += user.mention + " -> "
        self.gmMessage = self.gmHeader + LineMessage


    @commands.command()
    async def gmpls(self, ctx):
        """Request for GM buff"""
        try:
            self.addLineGM(ctx.author)      
        except:
            await ctx.send("{0} you are already in line for GM".format(ctx.author.mention))
        self.buildGmLineMessage()

        await ctx.send(self.gmMessage)

    @commands.command()
    async def gmdone(self, ctx):
        """Removes you from GM line"""
        try:
            self.removeLineGM(ctx.author)      
        except:
            await ctx.send("{0} you are not in line for GM".format(ctx.author.mention))
        self.buildGmLineMessage()

        await ctx.send(self.gmMessage)

