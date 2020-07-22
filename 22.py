def progon(st):
    check = ["АЛМАЗ", "ДАКОСТА"]
    for i in range(100000, 1000000):
        L = jarriquez_encryption(st, i)
        for j in range(len(st) - 4):
            if (L+"00000")[j:j+5] in check:
                for y in range(len(st) - 4):
                    if (L+"00000")[y:y+7] in check:
                        print (i, j, y, L)


def jarriquez_encryption(text, key, alphabet="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
    key = list(str(key))
    key = list(map(lambda x: (-1)*int(x), key))
    text = text.upper()
    L = ""
    for i in range(len(text)):
        L += alphabet[(alphabet.index(text[i]) + key[i%len(key)])%len(alphabet)]
    return L


c = "ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС"
st = c
progon(st)