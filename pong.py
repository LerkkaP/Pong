import pygame

class Main():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Pong")

        self.fontti_pieni = pygame.font.SysFont("Segoe UI", 27, bold=True)
        self.fontti_suuri = pygame.font.SysFont("Segoe UI", 50, bold=True)

        self.leveys, self.korkeus = 640, 480
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))

        self.kello = pygame.time.Clock()

        self.lataa_kuvat()
        self.pisteet()

        self.paikka1 = self.korkeus / 2 - self.kuvat[0].get_height() / 2
        self.paikka2 = self.korkeus / 2 - self.kuvat[1].get_height() / 2

        self.palloX, self.palloY = self.leveys / 2, self.korkeus / 2

        self.ylos1 = False
        self.alas1 = False

        self.ylos2 = False
        self.alas2 = False

        self.nopeusx = 6
        self.nopeusy = 6

        self.pallo_koko = 9

        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["lauta1.png", "lauta2.png"]:
            self.kuvat.append(pygame.image.load(kuva))

    def pelaaja1(self):
        if self.ylos1 and self.paikka1 > 0:
            self.paikka1 -= 7
        if self.alas1 and self.paikka1 <= self.korkeus - self.kuvat[0].get_height():
            self.paikka1 += 7

    def pelaaja2(self):
        if self.ylos2 and self.paikka2 > 0:
            self.paikka2 -= 7
        if self.alas2 and self.paikka2 <= self.korkeus - self.kuvat[1].get_height():
            self.paikka2 += 7

    def pallo_liike(self):

        tormays1 = self.kuvat[0].get_rect(center = (19 + self.kuvat[0].get_width(), self.paikka1 + self.kuvat[0].get_height() / 2))
        tormays2 = self.kuvat[1].get_rect(center = (self.leveys - self.kuvat[1].get_width() - 9.1, self.paikka2 + self.kuvat[1].get_height() / 2))

        self.palloX += self.nopeusx
        self.palloY += self.nopeusy

        if self.palloY + self.pallo_koko >= self.korkeus or self.palloY <= 0:
            self.nopeusy = - self.nopeusy
        
        if tormays2.collidepoint(self.palloX + self.pallo_koko / 2, self.palloY):
            self.nopeusx = - self.nopeusx

        if tormays1.collidepoint(self.palloX + self.pallo_koko / 2, self.palloY):
            self.nopeusx = - self.nopeusx

        if self.palloX <= 0:
            self.pisteet2 += 1
            self.palloX, self.palloY = self.leveys / 2, self.korkeus / 2
            if self.pisteet2 == 11:
                self.lopetusnaytto()

        if self.palloX + self.pallo_koko >= 640:
            self.pisteet1 += 1
            self.palloX, self.palloY = self.leveys / 2, self.korkeus / 2
            if self.pisteet1 == 11:
                self.lopetusnaytto()

    def pisteet(self):
        self.pisteet1 = 0
        self.pisteet2 = 0

    def lopetusnaytto(self):

        pelaa_uudestaan_valkoinen = self.fontti_suuri.render("Pelaa uudestaan", True, (255, 255, 255))
        pelaa_uudestaan_musta = self.fontti_suuri.render("Pelaa uudestaan", True, (0, 0, 0))

        teksti = pelaa_uudestaan_valkoinen.get_rect(center = (self.leveys / 2, self.korkeus / 2))

        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        exit()
                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN and teksti.collidepoint(pygame.mouse.get_pos()):
                    Main()

                if tapahtuma.type == pygame.QUIT:
                    exit()

            self.naytto.fill((54, 69, 79))

            if teksti.collidepoint(pygame.mouse.get_pos()):
                self.naytto.blit(pelaa_uudestaan_musta, (self.leveys / 2 - pelaa_uudestaan_musta.get_width() / 2, self.korkeus / 2 - pelaa_uudestaan_musta.get_height() / 2))
            else:
                self.naytto.blit(pelaa_uudestaan_valkoinen, (self.leveys / 2 - pelaa_uudestaan_valkoinen.get_width() / 2, self.korkeus / 2 - pelaa_uudestaan_valkoinen.get_height() / 2))

            pygame.display.flip()

            self.kello.tick(60)

    def silmukka(self):
        while True:
            self.tapahtumat()
            self.piirra_naytto()

    def tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos1 = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas1 = True
                if tapahtuma.key == pygame.K_w:
                    self.ylos2 = True
                if tapahtuma.key == pygame.K_s:
                    self.alas2 = True
                if tapahtuma.key == pygame.K_ESCAPE:
                    self.lopetusnaytto()

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos1 = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas1 = False
                if tapahtuma.key == pygame.K_w:
                    self.ylos2 = False
                if tapahtuma.key == pygame.K_s:
                    self.alas2 = False

            if tapahtuma.type == pygame.QUIT:
                self.lopetusnaytto()

    def piirra_naytto(self):

        teksti1 = self.fontti_suuri.render(str(self.pisteet1), True, (255, 255, 255))
        teksti2 = self.fontti_suuri.render(str(self.pisteet2), True, (255, 255, 255))

        self.naytto.fill((54, 69, 79))

        self.pelaaja1()
        self.pelaaja2()
        self.pallo_liike()

        self.naytto.blit(self.kuvat[0], (15, self.paikka1))
        self.naytto.blit(self.kuvat[1], (self.leveys - self.kuvat[1].get_width() - 15, self.paikka2))
        self.naytto.blit(teksti1, (self.leveys / 2 - teksti1.get_width() - 20, teksti1.get_height() / 5))
        self.naytto.blit(teksti2, (self.leveys / 2 + 20, teksti2.get_height() / 5))

        pygame.draw.line(self.naytto, (255, 255, 255), (self.leveys / 2, 0), (self.leveys / 2, self.korkeus), 5)
        pygame.draw.circle(self.naytto, (255, 255, 255), (self.palloX, self.palloY), self.pallo_koko)

        pygame.display.flip()

        self.kello.tick(60)

if __name__ == "__main__":
    Main()

