from chan.alokal_json import AlokalJsonChanHelper
from chan.chan2_jap import Chan2Helper
from chan.chan410_html import Chan410HtmlChanHelper
from chan.chan7_html import Chan7HtmlChanHelper
from chan.chanon_html import ChanonHtmlChanHelper
from chan.desuchan_html import DesuChanHtmlChanHelper
from chan.doushio_html import DoushioHtmlChanHelper
from chan.endchan_html import EndchanHtmlChanHelper
from chan.fchan_html import FChanHtmlChanHelper
from chan.hispachan_html import HispachanHtmlHelper
from chan.iichan_html import IichanHtmlChanHelper
from chan.chan_json import JsonChanHelper
from chan.json_kun import JsonKunChanHelper
from chan.kev4_php import Kev4PhpHelper
from chan.lolnada_html import LolNadaHtmlChanHelper
from chan.lynx import LynxChanHelper
from chan.mayuri import MayuriChanHelper
from chan.nowere_html import NowereHtmlChanHelper
from chan.plus4chan_html import Plus4ChanHelper
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
    ),
    "nowere": NowereHtmlChanHelper(
        28,
        "https://nowere.net/",
        "https://nowere.net/",
        "/res/",
        "/src/",
        (
            "b", "d", "tu", "a", "ph", "wa", "cg", "t", "p"
        ),
        rps=1 / 60
    ),
    "8kun2": JsonKunChanHelper(
        35,
        "https://8kun.top/",
        "https://media.8kun.top/",
        "/res/",
        "file_store/",
        ("1", "55chan", "_64chen", "8bantb", "8tube", "a", "_abdl2", "agdg", "amv", "aneki", "animu", "animus", "ara",
         "arda", "arms", "asatru", "asmr", "aus", "ausneets", "__b", "__baka", "_baneposting", "__baseballbat",
         "bcards", "bleached", "blog", "__bonehurtingjuice", "bq", "__brit", "bubblegum", "builders", "bunkers", "butt",
         "cafechan", "caffe", "canada", "cath", "chori", "choroy", "christian", "christianity", "christianmeme",
         "cicachan", "civicrs", "ck", "cloveros", "co", "cow", "__cuckquean", "cute", "cyber", "cyoa", "__czech",
         "dadtalk", "danpu", "dao101", "degen", "delete", "dempart", "desu", "diaperfags", "diaperfetish", "dir",
         "__dolphin", "dpfag", "_dpr", "druid", "_e9y", "eatme", "ebola", "eerie", "egy", "egypt", "etika", "eu",
         "euskotxa", "__exit", "f1", "fa", "fairy", "fallen", "fast", "faygo", "feet", "femaledomination", "feri",
         "__fightcomms", "film", "flemish", "floss", "fortnite", "freedomzine", "fukemo", "fumo", "fur", "furry", "g",
         "gamergatehq", "genesis", "_gesu", "ggis", "girltalk", "greenbreeze", "gts", "haxxor", "hentai", "hentaiclub",
         "__herm", "hermetics", "hgb", "hgg", "__hindu", "hisparefugio", "hissss", "hnt", "hover", "hybrids", "hydrus",
         "hypno", "_hypnochan", "icup", "imperium", "in", "ipfs", "ircsecrets", "islam", "ita", "jaooo", "jewess",
         "jmaatv", "joker", "jp", "k", "_kekforceusa", "kemono", "kocsog", "kohlchan", "__(komica)", "_komika", "kpop",
         "lain", "_lego", "leo", "lewd", "lit", "lol", "loomis", "loroy", "luddite", "magick", "maka", "mde",
         "merrychristmas", "miku", "milf", "mom", "monster", "msb", "mtb", "mtt", "mu", "n0thingness", "nanachi",
         "natiofr", "nep", "newbrit", "newsplus", "nobody", "nofap", "nofur", "nogatco", "nothingness", "ntr", "_nuke8",
         "oanda", "__ocb", "__ocult", "_omorashi", "opmk", "os", "otter", "p", "panconleche", "pdfs", "__peaceofmind",
         "pen", "philosophy", "_pkmns", "pnd", "pokeporn", "polymath", "pone", "projectdcomms", "__pyatibrat", "_qm",
         "qpatriotresearch", "__qresearch", "qrnews", "__rand21", "rec", "rmart", "rusrandom", "rzabczan", "s", "s8s",
         "sag", "sapphic", "shousa", "sikhi", "sip", "sl", "_snowboarding", "socpl", "strek", "subs", "__sve", "t",
         "tan", "tdt", "tech9", "techan", "techbunker", "tek", "templeos", "tenda", "teraha", "__texit", "tf2", "__tg",
         "_thb", "thedickshow", "throat", "_tibby", "tikilounge", "tkr", "tr55", "__trashcollector", "truthlegion",
         "tulpamancers", "turul", "tutturu", "tv", "u", "uaco", "_ucla", "underground", "__usersunion", "v", "vichan",
         "vietkong", "vietnam", "vore", "vr", "_warposting", "wdsc", "webm", "wg", "__wga", "wikieat", "wis", "wmafsex",
         "workrelated", "wqt", "wx", "x", "__xivl", "__xtian", "zoomerright", "zundel", "0", "55sync", "abdl",
         "alleycat", "_arisu", "arisubunker", "_arp", "bane", "_bimbohypnosis", "_bluemoon", "bmn", "brains", "cats",
         "_chance", "clang", "comfy", "critters", "_cursed", "_cvine", "cze", "d", "dcaco", "demonp", "_dnmd", "doomer",
         "doot", "elitabla", "_empanada", "erp", "_falseflags", "fashionplus", "fata", "femdom", "fit", "_flg",
         "_fr8chan", "futyitorna", "garrett", "_giantesshentai", "hentaiporn", "hmfr", "hooliedayz", "hsp", "hujszon",
         "iep", "just", "k46", "kind", "_kiwc", "kukichan", "_lacajita", "_legos", "lgd", "liveanarchy",
         "luciddreaming", "m", "_mapp", "mental", "_mets", "_milhis", "monarchy", "_myon", "newhomosuck", "newsci",
         "_nine", "oes", "onepiece", "_other369", "otomad", "_penguware", "psyid", "qresearch2gen", "rule34",
         "_satorare", "sonyeon", "split", "sunflower", "_tae", "test", "_tft", "tftg", "toy", "trap", "_vein",
         "_virtualreality", "vivian", "voros", "wbr", "_weird", "wooo", "yuuka", "fringe", "random", "cuteboys", "tech",
         "internatiomall", "interracial", "liberty", "htg", "mai", "komica", "cutebois", "argentina", "r", "tf",
         "draftnote", "abcu", "k117", "britfeel", "liberty", "htg", "mai", "komica", "cutebois", "argentina", "r", "tf",
         "draftnote", "abcu", "k117", "britfeel", "y", "an", "francofil", "portal", "royalhawk", "vdm", "bullmask",
         "imouto", "tripfriend", "arepa", "rwby", "sw", "y", "an", "francofil", "portal", "royalhawk", "vdm",
         "bullmask", "imouto", "tripfriend", "arepa", "rwby", "sw", "magali", "hikki", "biz", "eris", "india", "mg",
         "magali", "hikki", "biz", "eris", "india", "mg", "out", "infinity", "tifa", "muslim", "out", "infinity",
         "tifa", "muslim", "slackware", "archivo", "flatearth", "yaoi", "boombox", "wdp", "thedonald",
         "libertedexpression", "khyber", "jsr", "slackware", "archivo", "flatearth", "yaoi", "boombox", "wdp",
         "thedonald", "libertedexpression", "khyber", "jsr", "fso", "wumpawhip", "buddhismhotline", "indochinaexpats",
         "ett", "redbar", "skyline350gt", "asc", "bazafx", "bestkorea", "covid19", "sokra", "bowsu", "qpatriotsunited",
         "verzet", "wlctint", "cultstate", "melody", "vedic", "yhvh", "1cok", "astropolis", "fso", "wumpawhip",
         "buddhismhotline", "indochinaexpats", "ett", "redbar", "skyline350gt", "asc", "bazafx", "bestkorea", "covid19",
         "sokra", "bowsu", "qpatriotsunited", "verzet", "wlctint", "cultstate", "melody", "vedic", "yhvh", "1cok",
         "astropolis", "earthlibfront", "pardochan", "stanislawowski", "thetrump", "yukkuri", "1825kun", "cryptobtc",
         "isol", "knights", "language", "rr34", "sperg", "awaken", "belgium", "blizzard", "brain", "buddha", "dbs",
         "deestevensvoice4you", "f4net", "fuckuchina", "gbtv", "hairygirls", "hallaca", "homeowner", "indo", "jersey",
         "jigglypuff", "lbt", "madh4ckrs", "medcorp", "miamichan", "mrsfrisby", "mulatto", "mupro", "nhoodlink",
         "p5porn", "patriotrevolution", "peko", "projectobject", "prop", "pups", "qanonspain", "qcastellano",
         "earthlibfront", "pardochan", "stanislawowski", "thetrump", "yukkuri", "1825kun", "cryptobtc", "isol",
         "knights", "language", "rr34", "sperg", "awaken", "belgium", "blizzard", "brain", "buddha", "dbs",
         "deestevensvoice4you", "f4net", "fuckuchina", "gbtv", "hairygirls", "hallaca", "homeowner", "indo", "jersey",
         "jigglypuff", "lbt", "madh4ckrs", "medcorp", "miamichan", "mrsfrisby", "mulatto", "mupro", "nhoodlink",
         "p5porn", "patriotrevolution", "peko", "projectobject", "prop", "pups", "qanonspain", "qcastellano", "qsocial",
         "resist", "revolu", "skemt", "sketheory", "spaceforce", "surro", "thehand", "transit", "vitaecryptocurrency",
         "qsocial", "resist", "revolu", "skemt", "sketheory", "spaceforce", "surro", "thehand", "transit",
         "vitaecryptocurrency"),
        rps=2
    ),
    "hispachan": HispachanHtmlHelper(
        30,
        "https://www.hispachan.org/",
        "https://www.hispachan.org/",
        "/res/",
        "/src/",
        (
            "a", "ac", "c", "di", "f", "g", "hu", "k", "m", "mu",
            "p", "pol", "q", "r", "t", "tv", "v", "ar", "bo", "cc",
            "cl", "co", "ec", "es", "mx", "pe", "py", "uy", "ve", "d",
            "h", "o", "s", "sar", "scl", "sco", "ses", "smx", "spe", "sve",
        ),
        rps=1 / 20
    ),
    "sushigirl": JsonChanHelper(
        31,
        "https://sushigirl.us/",
        "https://sushigirl.us/",
        "/res/",
        "/src/",
        (
            "archive", "wildcard", "lounge", "arcade", "kawaii",
            "kitchen", "tunes", "culture", "silicon", "yakuza", "hell", "lewd"
        ),
        rps=1 / 30
    ),
    "4kev": Kev4PhpHelper(
        32,
        "https://www.4kev.org/",
        "https://www.4kev.org/",
        "threads.php",
        "/src/",
        (
            "anime", "cyberpunk", "design", "feels", "meta", "music",
            "politics", "programming", "random", "technology",
            "television", "videogames",
        ),
        rps=1 / 20
    ),
    "plus4chan": Plus4ChanHelper(
        33,
        "https://boards.plus4chan.org/",
        "https://boards.plus4chan.org/",
        "",
        "",
        (
            "baw", "co", "cog", "jam", "mtv",
            "coc", "draw", "pco", "coq", "cod", "a"
        ),
        rps=1 / 15
    ),
    "2chan": Chan2Helper(
        34,
        "https://<sub>.2chan.net",
        "https://<sub>.2chan.net",
        "/res/",
        "/src/",
        (
            "1",  # baseball
            "12",  # soccer
            "25<may>",  # Mahjong
            "26<may>",  # Horses
            "27<may>",  # Cats,
            "d",  # Animals
            "z",  # Plant life
            "w",  # Insects
            "49",  # Aquatic life
            "62<dec>",  # Outdoor
            "t",  # Cooking
            "20",  # Sweets
            "21",  # ramen
            "e",  # vehicles
            "j",  # moto & scooters
            "37<nov>",  # Bicycles
            "45",  # Cameras
            "48",  # Consumer electronics
            "r",  # railroad
            "img2",  # 2-D
            "b<dec>",  # Nijura
            "b<may>",
            "b<jun>",
            "jun<jun>",

            "58<dec>",  # ??? 二次元裏転載不可
            "59<dec>",  # ??? 二次元裏転載可

            "id<may>",  # 2-D ID
            "23",  # Speedgrapher
            "18<dec>",  # 2d-Live
            "16",  # 2-D Neta
            "43",  # 2-D Industry

            "74<dec>",  # ??? FGO
            "75<dec>",  # ??? アイマス
            "78<dec>",  # ??? ウメハラ総合

            "31<jun>",  # Games
            "28<nov>",  # Net games

            "56<dec>",  # ??? ソシャゲ
            "60<dec>",  # ??? 艦これ
            "69<dec>",  # ??? モアイ
            "65<dec>",  # ??? 刀剣乱舞
            "64<dec>",  # ??? 占い
            "66<dec>",  # ??? ファッション
            "67<dec>",  # ??? 旅行
            "68<dec>",  # ??? 子育て

            "webm<may>",

            "71<dec>",  # ??? そうだね
            "82<dec>",  # ??? 任天堂
            "61<dec>",  # ??? ソニー

            "10",  # Net characters
            "34<nov>",  # Narikiri
            "11",  # Original art
            "14",  # Original art flipside
            "32",  # Crossdressing
            "15",  # Bara
            "7",  # Yuri
            "8",  # Yaoi
            "o",  # 2-D Guro
            "51",  # 2-D Guro flipside
            "5",  # Erotic games
            "3",  # Homebrew PC
            "g",  # Tokusatsu
            "2",  # Robot manga and anime

            "63<dec>",  # 映画

            "44",  # Toys
            "v",  # Models
            "y<nov>",  # Models flipside nov
            "47",  # Models flipside jun
            "46",  # Figures
            "73<dec>",  # VTuber
            "81<dec>",  # 合成音声

            "x",  # 3DCG
            "35<nov>",  # Politics
            "36<nov>",  # Economics
            "79<dec>",  # Economics
            "38",  # Korean economics

            "80<dec>",  # ??? 安倍晋三
            "50<dec>",  # ??? 三次実況

            "f",  # Military
            "39<may>",  # Military flipside
            "m",  # Mathematics
            "i",  # Flash
            "k",  # Wallpaper
            "l",  # 2D Wallpaper
            "40<may>",  # Touhou

            "55<dec>",  # ??? 東方裏

            "p",  # Oekaki
            "q<nov>",  # Rakugaki
            "u",  # Rakugaki flipside
            "6",  # News desk
            "76<dec>",  # ??? 昭和
            "77<dec>",  # ??? 平成
            "9<img>",  # Idle chat
            "52",  # Great tohoku Earthquake of 2011
            "53",  # Nuclear power
            "70<dec>",  # ??? 新板提案
            "54",  # IPv6
            "layout<may>",

            "oe",  # ??? お絵sql
            "72",  # ??? お絵sqlip
        ),
        rps=1 / 3
    ),
    "waifuist": LynxChanHelper(
        36,
        "https://waifuist.pro/",
        "https://waifuist.pro/",
        "/res/",
        "",
        (
            "w", "starlet", "etc",
        ),
        rps=1 / 25
    ),
    "cutiegarden": LynxChanHelper(
        37,
        "https://cutie.garden/",
        "https://cutie.garden/",
        "/res/",
        "",
        (
            "lg", "cozy", "meta", "test"
        ),
        rps=1 / 25
    ),
}
