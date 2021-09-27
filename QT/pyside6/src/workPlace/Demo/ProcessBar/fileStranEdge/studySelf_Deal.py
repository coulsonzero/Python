import base64
import os
import sys
import traceback

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QHeaderView, QPushButton, QTableWidgetItem, QLabel


class dealStudy_main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 1000)
        self.IP = "127.0.0.1"
        self.DATA = [
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAMAAACJUtIoAAAAM1BMVEUXV4Xy+/8Asv9plLKfvdEya5TW5u8OebIUYpQCpu8Ij9GEqcIRbaO70uALhMJNgKMFm+Az1K8oAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC3UlEQVRYhe2Z7XbCIAyGIxSmIrL7v9phKR8BklJc55+95+yotYSHlxCog8v5EuN3RsF0iN+QqJS+qLH6rU+ioOMOYY33y2MQt52MNW4GGeEXsN6noFVhcaEHKdrrE7y0W2easauM9UmKRsBgCPTS10n0sAX/rDmift/PrX3IAzWIkZVKgXJG1190sWJXEqIWfIOBUk3QUSinjNUXbSWYqne2bkkVXnWNpYowyyzWkmG0czgIiSUYLEQyi7WgoM5hrKY8Ffq6htcb3NH1x1fx4Q63Zi1bB+BsHl9HGk2cnwCJsLgB9dzyvViwaNR667wgvd9uT/jmhvy44s/f6PaZ3IqXS6xS2+2LYmbX1umKp3ECK30SBJbZmjU9l/c0HS9QzPcE1nNro9coosWKzUBeSFUpvnZSpMZxLBGTc0vZDla4YqukRopBrFJrbIHNBa5OByyBsZZtVEZSWBZeWaUVWhkEloS0BMEwk1hCdt1SDgfu1K1XefB/zBym1neInqLlfngS4xIyQGOFXYumEjn0kvau5a3ccts11WD5LQ66UlJHmqTYSqUEdOXw2ENzBysWZ7+91ljKEblkVbPs4ixmszS8U7dkGlONZekM781zmLNslkTNj2LlMdVYzJbdJXb+ooG4YWCzMlavTLRYJncQsESBRVHhSpm6c2CAMOuoWypvhx5rPWt33cKDJObXr1fCLAor7Cseaz0ZJKyycL+ZW4Erm+VVkB1zy5XrvlmJamglFkYqdBRx01ilmiqv5U7dqmVw2IAlxrFuQ1iFD+ucMBt1GAYgs85yq2gX9kTDP65VZl0eJ2OlEwT77FGbdbpbI+et111V0HOxxM7pVMSYlVk7WEU6ZKx7G/5KuvUcOMu3ZkUs5jeI1DSqg5WrAfXkw+WW7hSS0UmclX9g1tpwZ+Y9vYvVrwDlU/WUTnErafpXpnOxpvWPdUQHfpf/S332P2SkPjiJnAPs5vM5/QAvRykt348iqAAAAABJRU5ErkJggg==",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAMAAACJUtIoAAAAM1BMVEUXV4Xy+/8Asv+70uBplLIya5RNgKOEqcLW5u+fvdELhMIIj9EFm+AUYpQOebICpu8RbaNmpojSAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADnElEQVRYhc1Y6XqDIBBEbhJNfP+nLccucqpYm2a//jDjFobZA4RMX2nkvwm0rUWLfppEPeG3qvVxaU6ZV+s2arcNlATxL3S7OubX5tbpBe073qu1TXlKz1P7lEEQ76PWHGZ47DTla2aMC0GEVCwfv4I73tctT/lcNCaEYnrSjBOur8CSoCV+TSsFqSsxMlNEIaYliRLk8NyGg7eUATA7tNrxbTYILxonaTA4MfhwHj5Dq23dvvUgz2whoIDyE9I2XHrfQKsQUxOeF4EWAuHMbw/u0zoqTdJpDRxG2l4blzy8mmAPlmuP1hFLgnMX7NLlwzsnQKnKPrwTRKakILabdHimuZWQM6RoPvaFIrqCJ5dWORzrWNONFoutwheslotvJryX2vG8FbXy3B7ob4tdwlJnMrdgRphqwwmthSPqco4J8FJdWvlPJMcFBFZKjUprYvgCchawgH/NYR9E6mmR2GCZqweM3VlaaH4iZ8uDvpZAJc5vfwoVXRD23hmc5JbBB+UHB5J0lJbCiWD9Trg3mS3sGdJ1fW+ysNIb4I0WqIbdJPa4UVomyZZtqdMT+4mDn1gdpTfFESItqIiwFSRc4uPxnhjXGh/hgUuAadAONynZ8460wFjoIwk6qtYkOS5BYU8SKsAwIoeisNmXwal3TkuGnBJbkxumxWIHFCxBWvCb0pm8W94lrfATjxpa2uPZIK1JwZAM05nLPXgN0uUw0oKlQNdFWso110NaZdY9wpgxPsKkdOWrhi2t9QU7hYfLlPdVSpGW7RPszOZTmJEsyX0bFbrB75D7SVTBe/aF6qLqezFUJSwtyLXR6s8daLXPGVpyrfJgVfCrhp1cwXsNod226kUO0dosJ8hEzM/0nDe34dT76VSDINIneVBoZqZFa/jGJh6kYsf0YzTg2ttmWtx8BHS7ZYm06Iha5WuMkeQXYLmGPcFu1ZChysropLMfzUNBzM1sUWEXYB9Ey8GqFetZBLUsikeAYHkg91LenUPg6KxEC54OYGwQNrfiK2LS3GqcixNaPbNfomHdQuXwqw0X3smhWTxgdiIalViRO7pIMqtQOtlzEJZn4IQWtg7X21sNgk6ZdMf3W9p+DMg6O8/Ayce+JrXV/x0Oc9ZOXbtpZa7AvYw9cT30X7eBB8x+Qeu3F2J7ot2v1hDbHrW/UOsMsbSRDvetDxh1f5Vo/04rWsasS+tiQv+qDjbR2reBd841aIHa9wQxMUp/AJvfLa6f2XRuAAAAAElFTkSuQmCC",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyBAMAAABMoj8pAAAAMFBMVEUXV4Xy+/8Asv8Fm+AOebIUYpQya5RNgKOEqcK70uDW5u9plLKfvdEIj9ELhMICpu8MuOs7AAAACXBIWXMAAA7EAAAOxAGVKw4bAAACuElEQVRIic1XO4/UMBD2VewLCQe0e8lGQjZ0CCHxDyiuR0hIdLANy6OB5tDdNdnm0FFtGmgvzemg2m0WiWqXhpY/AfwNxokTj+048T2EGCleJ/Z8833jiZ0l9PKMOJ4Hl4jVbkyPzTlHWEFtt80ECBjDvFjD/HpTINLOo7EA4RZ7T6wiutTjGvbDCiw9asiLF7NBmtdEYRlB3UzMeFUQmxd3JcUBU8cr13Nr5+H0yPYrtTHRY64CIhQnJXx+lH1efGsmNCZgg5pYREtKMoMmepM6pQin8QTm6FiKV2V3ukXguomIl4Yl0KUwDSvZFL+I2Ceyh0gFCosjYzavqC87J5NSXDz4klTAMvztR5zfu9qicdyTnbhTPjr+zu8+ReGZpdGBdW1Z/HL+uHT/Bc4mhTasnP7P+2WZJpkcXsHVN1wAK6jHQtlLqCiIfWjnqRxeZPR6R/cIvDQCCTban0LvWC4onb+iJ3mhoDLzxaLD2Qpjjcg7srQ1tmMdCueCV1oKWhAzXRWW9VJirDUV+RrIXrhLlL3O1DQvXjmbaAuar3AN99DQx7cGllYogY01WkKz/QCaFxStpbC4p/o33LyU7FA4DFPZWSNZNOwavJwaS7g/Qo2YLRSt8bSoq0L67TnbgHEguG0krwrA4MXaseiPNBJOcyFP5KvCwvlSvIxjSceKDk7FdiOWkQ5folTidWzIvWbhs1k58eZKr68KGOdLq1fzTFtkjMZb6J50TB+/3INdobLOpB+8j7PyhmGsmmPNwMp31OptLPaJnpFjL17gMhLrdagewf4VGvuXt8ZxHzg9UfeOfdUvX/HuhxDV0m+4crciPexMWDR6P52oO9gUcZkWvOxvAAcWpacb1a/OR5/P2bbvQnxuXxTrLNaKVdVWu8p/ysttjefQRe1/wWJyYcrlqf+fdj77C6TBVJki9EcVAAAAAElFTkSuQmCC",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyBAMAAABMoj8pAAAAMFBMVEUXV4Xy+/8Asv+70uBplLIya5RNgKOEqcLW5u+fvdERbaMFm+ACpu8UYpQOebIIj9F09ob9AAAACXBIWXMAAA7EAAAOxAGVKw4bAAADdklEQVRIia1XzW7TQBB2lTZNEapY2/EPcIkREhI92FKLOKZUqTg2Ek3FLZEKlJutqhUXpERQVdycCxJvwEuABE/CA3DhDZiZ3fXPxhu7UUfy/u+338zOTDZGj5GYTJXeQqNOjKYLbw+rlpu5HMus0rwRlrqtsZVy0fFaAarGXivqeAvSAEuqW0uyGmuJ5y5Z1lzHetspWNbgaHSuX+28nzXGso7PZ5/6L3knNkDWZUUyHbTnepZlrDiBwhtH1OkOoQhnr7DZ4fMf2a5xIBf3VMwSlt2iOXuLKn8TtTpAmDThCwDXH+830jEWCghix/BZ7YlogTxoAZt03gTLE1ZhV0OqiM0YtrpbgjeOj3VQJSxbWIVrB1ZaA11DJiyHdVI4MBdpsyLWvcwSXCcLIX2W6x6CR7itRrzSSLbiGV3SWHjTSAwfwnd/Y94EK2boEGdIgKOGCVWCisnQbNNvI52/FrEG8DlnSGLKz3a4AacTbhMfuxfZTWiwehlWNxnkWBa/g5izZA66xwlje4kGKwg4fzoS1n8nXmJ3H9XJbg5PeATcPA0x4BUEAeeV4sbxlmjRbmSQuQra08a7TksWy8LIIJiA2BEbbw2KQzFPMJmrnKINIsb9rJoXF4BzcJO7DwediEFnKAo80WtB+QyH3aEWS5J8ejfgB1tSK4o9cQPMR8Z9TBt+h1VJKbYvgd0PONyeiAHu/+CypmSzeQX6WdW+X8JyAePUDILHc9HnFyZcFk/wOmh8r4BV+CEQWELNrxEtC3/zm+1yfsJlKUu8bsqLeafXsKEHcWeio8QRjVrcwWy01x62m9gLth0lmS+aO3eEAjzG/YwNodZikaf7YqndAnZ/oRGSh+WZqzspb+pVY7Xhc17wWYzpJ+vgeMLzZQpimjStYFFGldGIad81AGBnm4J2KgNgxCpFwXJ4WiEhk3cHCZT9CKMsS/vVplex7PWIyQgi3PALlqgt+PGffzQhU/YSLPIx/80HGUEpqvSWkG1+he42espnXcZfeGN6l6Mhbx3hj3+LpVi1+dDeyfOHP7d/1WHlci1VKPy+y0jZPd54NzNlwlNmIa8GMhlq36iLE2bVFiOby0UHuQCnrKx6yxVxFUqlrsnKcCqW+q4yVVx1QQHuJu9onSFkb+U3edkQVGiwbva3QxDW8dK8mpc+po3V/vpUyn/SUU6c0gHNXwAAAABJRU5ErkJggg==",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAMAAACJUtIoAAAAM1BMVEUXV4Xy+/8Asv8Fm+BplLIya5RNgKOEqcLW5u8LhMICpu8Ij9EUYpQOebKfvdG70uARbaN3R7NdAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADa0lEQVRYhc1ZWWLrIAyUCVvSxPT+p33GbJLY7D4nrT7aBFNpGK24IJa/KEC/9kAK+vntZ6Gwjpk7sus/gcN8yym5iMerYV0kIMSfCXoExLMlfhday3ZyovgotqklEluHoF0Ffqinqlufpa0n7UycQftwOSWmN7lJpUBpY4c6rgQpZrCWxUq43x7Cfkkw5IGBLJJ/q3Zk0SfQDWBZpXeWPGtPSR4pFT84sItKzxRkVk2l18F6DSyFjmefLxxta6ZPS5fArIjTGpaEcSQchWVU1COCTYeTFNGlE/q81oSFn56DRULX5rOH5WQ9QEN0JecY7KUKlmXheQIWkZWRbtD3Ddkz/aFLHwgdFSzPNpNRAnfnLROsWB2P6aheB/fo0RZZNSx9yod9tmTQo7UNeCzLJO3Zw9FG8r+CBXI5Kl7nYVg8wV2JPQ/NUDI5rKo8ND0o8jE7sERSnJ0Yg6Oo0zj4HvBN2lUup9nFk0bBWnGXLX4+yXc6nFs7WXWXz8VKdUs8BzSBxTTZOjhQgURPiZGkg5YHMQI0gWVRwou9bFY7ii1WwpO9TCitNmIEqA0rb9YsGtbNqUxTAdPKs83wPW3w+SOWMUFDWAmaq6pyXXnKCnkW7W4/1TOiAHkYUB+WlyrCd7p6C/UhvAQv+wEEbiMMDbTQfCZysK4KdPQE9xTuNtzlu9zhFhgycHYU77GVW85qY2Etc1WQ2G1E3EdSLUh2bWzzE2j42QSW9ApjAdc0F2kBiXThEEpVQ4S+JQriYZfuVXmBYUkEi7BleOt+cTLy0MCHkRFtk1k+eqzrRFvqWPRYFV066Zat6WEcbd1MjKpKyNMRQqZp9fVY4gF47coLKsZdjaILrQdrhUe1gubA3JpL2+HDeq4frp4AObTjPVHxw4eFGNM6mdpGhYiGd81XUl3P9W1sh2DxKVc+H+Vvi8eUTC7a/Yo1p+AjqTLIQUzb4OaTrYi9vWGbOb6329ha6MIlY0sWEZfPXBBTt+rvMPCVypClTKyZLF/L2nTJcn2k08UhaL3pdH8DoZRxdrHO5AYURJUbvPN2W/d59aNLfpIKFmn1a3w1MkyldwiCdXL2eOvbpB1WH9DM9LteHsKUoV95NfiJ9/KC/T4gH/l3wXnCT8P6jE//6j9XLtVGqezk0k8vZMcxcAuXefgfPwopd0tiggkAAAAASUVORK5CYII=",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAMAAACJUtIoAAAAM1BMVEUXV4Xy+/8Asv9NgKNplLKfvdEya5S70uAUYpQOebKEqcLW5u8Ij9ECpu8Fm+ALhMIRbaPTNLpaAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADxklEQVRYhc2Z2YLqIAyGU5agxFne/2kPO4ECrTPVObmxrZR8JD8BFLb/xQS/gTf6eqIhLL99txX3MHj2Mmfn7YokXjoeEWyGtXR1fVxFsXgPr3JUHJ5hEX3TF8/EY5axvQlrHpexvRLrXGCGdjnWL1iY/RIru04gH4874r5LBmiUa4DSmp9jSeCm9t66wBgpNZGFDctLHZtBtIY2MgoU/RQLNLtBNWappjCEwGOltrbr3YLNlyRhFbAFlmEvCnG7HwiGsUywVEOi0qiHPS6wLPDA4D6JjUlZXptg2Sb6XiPzeO2wKspd8ucdVj9GDVkrMyyK6qwvEuKISDCskWBakF20WjAsqtlhpYYKmMhFHIrdGqtdwlQx1MacY+kwy1HVBsb5FAMsN5nRRpzBVL4NwxUaz75wY2lSn1w539qVHfKz3CJmMFUdcCxpfKUK49PwuXNhYwAHQZljddOoREthDZLOT4vglatZfcK15yrdudIgUzrNVPRzrOyJ2nIqkddBQtlAO7nQXofWvVPiKWV+qdGJaD76OsyAU99kXQAKi8K2Opso26om2EfL9WUrFtbrTr78hclz54/lCkDun2YQ2pr4ZG3xQSrpIpaum2g9nUTN5zNhip2UfTsK4RpjCfZMM23lsene++jk036pgDd0AqOti3quRzjG6sbIIkPZqdoNcoUVDHnN8R2rbb/2JpeHWL6sfZeHNl9hW07P7OWV9rWpKjysFEW3RpbqGGb5GOsj+/VtTFEFmgo7saNtYAEJ0i7SQkXZ9wLLZp2HNjZPm9zlPIeHWKXihQsp643ls3yCpTlW5pIlh4/nsaxOHfKKzAqOm1BbkMN5rE37xYjgOIcVq62yfiaCMkQlbTEPubn2M6IgVizVlNMeyxUHRfZEDheSR3caACxb7jC2ZhEbYgWfUywvrLybIRjlUDS/QfSxavYE0UV0yEZ4gCV6rNh52Xbp3VaP7bAW0Wrvo1D5budH0dr8MhYAvleHg7NYeS1iS/UAS4yxhIHPFI0HfEWS+Xr4BBaVglw3NkdJFOLrcYswn4VB5hza6c70PBaxAiDzNrDFEgHkHjjC4W0bJtGdW+Nlt/DMsHaHUectP9PNIuc3zf5oDFEkH/CoIMfacsXLr7SrorUtouXqSzqY5y17+g3IC+R+u7GfAXy08nXEKt+UNqbpWqJc5nC5+KQDzv3RzuArfjkkO9uXrrBGpWTU7DdkS8tYw6L2dwbPgLwed1nln3d/NfD/8p9PZ/Nz4slOX5PYS/+Kug6xzMS/QxjZ2//FOGf/AHvNLY87gS+xAAAAAElFTkSuQmCC",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAyCAMAAACJUtIoAAAAOVBMVEUXV4Xy+/8Asv+70uBplLIya5RNgKOEqcLW5u+fvdEIj9ELhMICpu8OebIUYpQRbaMFm+A/dZtUhKZM6rdFAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADP0lEQVRYhe2YW5ujIAyGU860dtrd//9jV5AgpwC2+szN5mqaQfLyJQYEbpcZ++JZOI3iVPuPVVsjzcF1DdY3ZeXtAizW/TlnH2LNxvpUtgTra+XbdqJaU1NdtAxvTayTA7Lqj6FRtXWlFBPWLXnGhZQglTa53wY3H82ulDWjMYexuJKam5vhAnTqlsGtpeoHNSAkKPsJFp0tu8MY5QC2oRpiHCNgF6wxkZbrIgSAGMq6z7IZrZaFdJlKRXcaQ8O7E0OK7REFoo5foXgLLhLLZImLIZbCrSRNxXEF+QpLkla+SKwyXohRuk0VcTeBYxWUKOQzAywO95JTNSkELZfUG8oCzxmUGSxd/cNC082hqOeoyBsWfEnmSz5itVcRSzyacZMLdCusMa9fMz/JWHm0SVBqhQp3TQqndPHRbeEBAePnSeQH872C21GHO4olAP+6gV77yWNjuYOFEKjWFclDq3PdK+12Z2BZQJLFvQSYOj3Gin7pn+FSt8dNYzmI5w/KguF9H/VYbAZrQXl4GNhqJeTbiVhl0WJUGduncp6WWn9gt72C4jsrgu7Mwnx9QYKS2ZZFGyMZcKq0sXhYNvrcL4UlKWN3OJBGwGlK2/a+XaxtV66xmMfCZ6IeBp18z7HubFQtrKapdWINONMmFqlWhWVjDvdXeS6LrI/lOiYUYtFYWUHeEmVAG0zeuiHM7kC9Y+B6UirEmlcLW7xZXVj0prUJEa24xywSsVZTLGLZDpYPFHdwaVO1etGmsWRWo65B7V02NgD5t9UgBARALuFYbQ2xig3DYRFbdW22oYzIg/XqrINlIH+hHVbrYNOUwDTOyZLYpo5hlburWmtr/hioKlx3dCYVYrnRWKVY2+Y3fWhO5fIw7OfFaCuepq9GRBkwnJrpT4w80APu2W9xYEvsffmU2Vmx/JHincVeyBXn6zp24CqxYoxnsVjGXi9WzJ99vtamQx7ZcGSNReTYQG3hRRp+7MdJ4kgBYpDBQmr45HKmdzWSz0bcrZA4CdaczcGfdf/UPDSfNHfHRiEqLNb5dXTyD6y8l6dD9O4YrxK2UOubMGcipli/fF+aIkDq+Q0u4nR6Bcr3c071reveOMr+AT+MKP+NhOcyAAAAAElFTkSuQmCC"
        ]

        self.table2 = QTableWidget(self)
        self.table2.setGeometry(5, 35, self.size().width() - 10, self.size().height() - 40)
        self.table2.setColumnCount(2)
        self.table2.setHorizontalHeaderLabels(['图片', '结果'])
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置列宽的适应方式:自动.

        self.table2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.table2.setColumnWidth(0, 300)


        self.updatebtn = QPushButton(self)
        self.updatebtn.setGeometry(5, 5, 80, 25)
        self.updatebtn.setText("刷新")
        self.updatebtn.clicked.connect(self.updatebtnDo)

        self.submittn = QPushButton(self)
        self.submittn.setGeometry(100, 5, 80, 25)
        self.submittn.setText("提交")
        self.submittn.clicked.connect(self.submittnDo)

        self.show()

    def updatebtnDo(self):
        self.table2.clearContents()
        self.table2.setRowCount(0)
        try:
            self.table2.setRowCount(len(self.DATA))
            rowcount = 0
            for index in self.DATA:
                paths = "C:/test/temp/%d.jpg" % rowcount
                if self.writeJpg(index, paths):
                    self.table2.setRowHeight(rowcount, 100)
                    temp = QLabel()
                    # temp.setGeometry(150, self.Heights - 49, 24, 24)
                    temp.setStyleSheet(
                        "QLabel{border-image:url(%s)}" % paths
                        )
                    self.table2.setCellWidget(rowcount, 0, temp)
                    self.table2.setItem(rowcount, 1, QTableWidgetItem("测试"))
                    rowcount += 1
        except:
            traceback.print_exc()


    def submittnDo(self):
        sendData = []
        for index in range(0, self.table2.rowCount()):
            if self.table2.item(index, 1) is not None:
                if self.table2.item(index, 1).text().strip() != "":
                    sendData.append({
                        "base64Code": index,
                        "result": self.table2.item(index, 1).text().strip()
                    })
        self.table2.clearContents()
        self.table2.setRowCount(0)

        print(sendData)


    def writeJpg(self, datas, paths):
        try:
            if not os.path.exists(os.path.dirname(paths)):
                os.makedirs(os.path.dirname(paths))
            with open(paths, "wb") as f:
                f.write(base64.b64decode(datas[datas.find(","):]))
            return True
        except:
            traceback.print_exc()
            return False


    def resizeEvent(self, event):
        self.table2.resize(self.size().width() - 10, self.size().height() - 40)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    cilentUI = dealStudy_main()
    sys.exit(app.exec_())
