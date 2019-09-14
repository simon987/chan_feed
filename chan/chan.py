from chan.alokal_json import AlokalJsonChanHelper
from chan.chan410_html import Chan410HtmlChanHelper
from chan.chan7_html import Chan7HtmlChanHelper
from chan.chanon_html import ChanonHtmlChanHelper
from chan.desuchan_html import DesuChanHtmlChanHelper
from chan.doushio_html import DoushioHtmlChanHelper
from chan.endchan_html import EndchanHtmlChanHelper
from chan.fchan_html import FChanHtmlChanHelper
from chan.iichan_html import IichanHtmlChanHelper
from chan.json import JsonChanHelper
from chan.lolnada_html import LolNadaHtmlChanHelper
from chan.mayuri import MayuriChanHelper
from chan.russian_json import RussianJsonChanHelper
from chan.synch_json import SynchJsonChanHelper
from chan.tgchan_html import TgChanHtmlChanHelper
from chan.zerochan_html import ZerochanHtmlChanHelper

CHANS = {
    "4chan": JsonChanHelper(
        1,
        "https://a.4cdn.org/",
        "https://i.4cdn.org/",
        "/thread/",
        "/",
        (
            "a", "b", "c", "d", "e", "f", "g", "gif", "h", "hr",
            "k", "m", "o", "p", "r", "s", "t", "u", "v", "vg",
            "vr", "w", "wg", "i", "ic", "r9k", "s4s", "vip", "qa",
            "cm", "hm", "lgbt", "y", "3", "aco", "adv", "an", "asp",
            "bant", "biz", "cgl", "ck", "co", "diy", "fa", "fit",
            "gd", "hc", "his", "int", "jp", "lit", "mlp", "mu", "n",
            "news", "out", "po", "pol", "qst", "sci", "soc", "sp",
            "tg", "toy", "trv", "tv", "vp", "wsg", "wsr", "x"
        ),
        rps=3 / 2
    ),
    "lainchan": JsonChanHelper(
        2,
        "https://lainchan.org/",
        "https://lainchan.org/",
        "/res/",
        "/src/",
        (
            "λ", "diy", "sec", "tech", "inter", "lit", "music", "vis",
            "hum", "drg", "zzz", "layer", "q", "r", "_cult", "_psy",
            "_mega",
        ),
        rps=1 / 60
    ),
    "uboachan": JsonChanHelper(
        3,
        "https://uboachan.net/",
        "https://uboachan.net/",
        "/res/",
        "/src/",
        (
            "yn", "yndd", "fg", "yume", "o", "lit", "media", "og",
            "ig", "2", "ot", "hikki", "cc", "x", "sugg"
        ),
        rps=1 / 120
    ),
    "22chan": JsonChanHelper(
        4,
        "https://22chan.org/",
        "https://22chan.org/",
        "/res/",
        "/src/",
        (
            "a", "b", "f", "yu", "i", "k", "mu", "pol", "sewers",
            "sg", "t", "vg"
        ),
        rps=1 / 120
    ),
    "wizchan": JsonChanHelper(
        5,
        "https://wizchan.org/",
        "https://wizchan.org/",
        "/res/",
        "/src/",
        (
            "wiz", "dep", "hob", "lounge", "jp", "meta", "games", "music",
        ),
        rps=1 / 60
    ),
    # TODO
    # "1chan": ChanHelper(
    #     6,
    #     "https://www.1chan.net/",
    #     "https://www.1chan.net/",
    #     "/res/",
    #     "/src/",
    #     (
    #         "rails"
    #     ),
    #     rps=1 / 600
    # ),
    "2chhk": RussianJsonChanHelper(
        7,
        "https://2ch.hk/",
        "https://2ch.hk/",
        "/res/",
        "/src/",
        (
            "d", "b", "o", "soc", "media", "r", "api", "rf", "int",
            "po", "news", "hry", "au", "bi", "biz", "bo", "c", "em",
            "fa", "fiz", "fl", "ftb", "hh", "hi", "me", "mg", "mlp",
            "mo", "mov", "mu", "ne", "psy", "re",
            "sci", "sf", "sn", "sp", "spc", "tv", "un", "w", "wh",
            "wm", "wp", "zog", "de", "di", "diy", "mus", "pa", "p",
            "wrk", "trv", "gd", "hw", "mobi", "pr", "ra", "s", "t",
            "web", "bg", "cg", "gsg", "ruvn", "tes", "v", "vg", "wr",
            "a", "fd", "ja", "ma", "vn", "fg", "fur", "gg", "ga",
            "vape", "h", "ho", "hc", "e", "fet", "sex", "fag"
        ),
        rps=1 / 5
    ),
    "endchan": EndchanHtmlChanHelper(
        8,
        "https://endchan.net/",
        "https://endchan.net/",
        "/res/",
        "/.media/",
        (
            "art", "film", "oekaki", "draw",
            "adv", "r9k", "hope", "spoon",
            "a", "am", "amr", "l", "monster", "m", "2hu", "animach",
            "b", "webm", "v", "vvv", "vidya", "tg", "otomad", "mu",
            "metal", "tv", "f", "clipuploads",
            "4", "deutsch", "j", "jp" "italia", "fr", "kc", "kurenai", "int",
            "intl", "lang", "librejp", "rzabczan", "55chan",
            "pol", "pdfs", "his", "ggrevols", "horror", "aethism",
            "tech", "g", "markov", "os", "agdg", "cyber", "HTML", "2600",
            "ausneets", "qanonresearch", "polru", "yuri", "christianity",
            "kc", "rapport", "news", "brit", "webm", "4chon"
        ),
        rps=1 / 10
    ),
    "38chan": JsonChanHelper(
        9,
        "http://38chan.net/",
        "http://38chan.net/",
        "/res/",
        "/src/",
        (
            "a", "b", "g", "38"
        ),
        rps=1 / 600
    ),
    "alokal": AlokalJsonChanHelper(
        10,
        "https://alokal.eu/",
        "https://alokal.eu/",
        "/",
        "src/",
        (
            "b", "pol", "sk", "int", "slav", "s", "gv", "mda", "sp",
            "fit", "had",
        ),
        rps=1 / 60
    ),
    "gnfos": JsonChanHelper(
        11,
        "https://gnfos.com/",
        "https://gnfos.com/",
        "/res/",
        "/src/",
        (
            "jp", "drive"
        ),
        rps=1 / 120
    ),
    "synch": SynchJsonChanHelper(
        12,
        "https://syn-ch.ru/",
        "https://cdn.syn-ch.ru/",
        "/res/",
        "src",
        (
            "b", "d", "_r", "a", "_g", "mlp", "mu", "_tv", "vg",
            "_wh", "old", "test"
        ),
        rps=1 / 120
    ),
    "tahta": JsonChanHelper(
        13,
        "https://tahta.ch/",
        "https://tahta.ch/",
        "/res/",
        "/src/",
        (
            "b", "g", "s", "v"
        ),
        rps=1 / 300
    ),
    "awsumchan": JsonChanHelper(
        14,
        "https://awsumchan.org/",
        "https://awsumchan.org/",
        "/res/",
        "/src/",
        (
            "an", "aw", "cr", "fi", "ra", "au", "ga", "he", "sp"
        ),
        rps=1 / 600
    ),
    "horochan": MayuriChanHelper(
        15,
        "https://api.horochan.ru/v1/",
        "https://%s.horochan.ru/src/",
        (
            "b",
        ),
        rps=1 / 20
    ),
    "doushio": DoushioHtmlChanHelper(
        16,
        "http://doushio.com/",
        "http://doushio.com/",
        "",
        "/ass/",
        (
            "moe",
        ),
        rps=1 / 20
    ),
    "desuchan": DesuChanHtmlChanHelper(
        17,
        "https://desuchan.net/",
        "https://desuchan.net/",
        "/res/",
        "/src/",
        (
            "bananas", "boku", "dawa", "desu", "jum", "kashira", "md",
            "otousama", "ro", "unyuu", "yakult", "a", "c", "h", "_loli",
            "moonspeak", "nagato", "nij", "nipa", "touhou", "tr", "yan",
            "yan", "vn", "do", "fi", "lit", "o", "pro", "tech", "v", "vic",
            "arrrrr", "brocastan", "gar", "gif", "media", "ot", "r", "w",
            "sandbox", "sugg"
        ),
        rps=1 / 30
    ),
    "aurorachan": DesuChanHtmlChanHelper(
        18,
        "http://aurorachan.net/",
        "http://aurorachan.net/",
        "/res/",
        "/src/",
        (
            "_bm", "de", "ic", "rp", "rpi", "v", "w", "tg",
            "alt", "b", "g", "pkmn", "yuri", "fl", "mu", "sugg"
        ),
        rps=1 / 20
    ),
    "tgchan": TgChanHtmlChanHelper(
        19,
        "https://tgchan.org/kusaba/",
        "https://tgchan.org/kusaba/",
        "/res/",
        "/src/",
        (
            "draw", "meep", "quest", "questdis", "tg", "icons",
        ),
        rps=1 / 600,
    ),
    "lolnada": LolNadaHtmlChanHelper(
        20,
        "https://lolnada.org/",
        "https://lolnada.org/",
        "/hilo/",
        "/src/",
        (
            "b", "a", "aw", "cgl", "dw", "int", "qt", "sad", "t",
            "toy", "v", "x", "34", "e", "f", "h"
        ),
        rps=1 / 60,
    ),
    "fchan": FChanHtmlChanHelper(
        21,
        "http://fchan.us/",
        "http://fchan.us/",
        "/res/",
        "/src/",
        (
            "f", "m", "h", "s", "toon", "a", "ah", "c", "artist", "crit", "b"
        ),
        rps=1 / 60,
    ),
    "0chan": ZerochanHtmlChanHelper(
        22,
        "https://0-chan.ru/",
        "https://0-chan.ru/",
        "",
        "/assets/",
        (
            "0", "0ch", "0chan", "1chan", "2ch", "3dprintor", "8", "\\_b", "a",
            "an", "asylum", "bb", "bo", "c", "copypaste", "dog", "draw", "e",
            "elite", "eot", "ergrgergre", "fido", "fur", "g", "game", "hui", "huz",
            "hw", "ithub", "m", "meta", "naotoudigu", "nhc", "nullchan", "parasha",
            "poligon", "postach", "psih", "r", "rm", "s", "shrek", "shy", "t",
            "test", "tlp", "tmp", "tv", "vg", "vipe", "wh", "xikkadvach", "ynet"
        ),
        rps=1 / 5
    ),
    "410chan": Chan410HtmlChanHelper(
        23,
        "http://410chan.org/",
        "http://410chan.org/",
        "/res/",
        "/src/",
        (
            "d", "b", "cu", "dev", "r", "a", "ts", "ci"
        ),
        rps=1 / 120
    ),
    "7chan": Chan7HtmlChanHelper(
        24,
        "https://7chan.org/",
        "https://7chan.org/",
        "/res/",
        "/src/",
        (
            "7ch", "ch7", "irc", "777", "VIP", "civ", "_vip6",
            "b", "banner", "fl", "gfx", "fail", "class", "co",
            "eh", "fit", "halp", "jew", "lit", "phi", "pr",
            "rnb", "sci", "tg", "w", "zom", "a", "grim", "hi",
            "me", "rx", "vg", "wp", "x", "cake", "cd", "d", "di",
            "elit", "fag", "fur", "gif", "h", "men", "pco", "s",
            "sm", "ss", "unf", "v",
        ),
        rps=1 / 30
    ),
    "chanon": ChanonHtmlChanHelper(
        25,
        "https://chanon.ro/",
        "https://chanon.ro/",
        "/res/",
        "/srs/",
        (
            "a", "int", "j", "m", "pc", "pol", "prog", "tv",
            "b", "milo", "pr0n", "s", "c", "sug",
        ),
        rps=1 / 60
    ),
    "chanorg": JsonChanHelper(
        26,
        "https://chan.org.il/",
        "https://chan.org.il/",
        "/res/",
        "/src/",
        (
            "b", "goys"
        ),
        rps=1 / 60
    ),
    "iichan": IichanHtmlChanHelper(
        27,
        "https://iichan.hk/",
        "https://iichan.hk/",
        "/res/",
        "/src/",
        (
            "d", "b", "bro", "ci", "cu", "dev", "gf", "hr", "l",
            "m", "med", "mi", "mu", "o", "ph", "r", "s", "sci",
            "tran", "tu", "tv", "x", "es", "vq", "au", "tr", "a",
            "aa", "abe", "c", "fi", "jp", "rm", "tan", "to", "ts",
            "vn", "vo", "misc"
        ),
        rps=1 / 10
    )
}
