

                    self.player.get_input()
                    if self.player.move(self.grid) == False:
                        self.reset()