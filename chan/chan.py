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
from chan.infinitynext_json import JsonInfinityNextChanHelper
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
    ),
    "horochan": MayuriChanHelper(
        15,
        "https://api.horochan.ru/v1/",
        "https://%s.horochan.ru/src/",
        (
            "b",
        ),
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
    ),
    "8kun2": JsonKunChanHelper(
        35,
        "https://8kun.top/",
        "https://media.8kun.top/",
        "/res/",
        "file_store/",
        ("1", "55chan", "_64chen", "8bantb", "8tube", "a", "_abdl2", "agdg", "_amv", "aneki", "animu", "animus", "ara",
         "arda", "_arms", "asatru", "_asmr", "aus", "ausneets", "_b", "_baka", "_baneposting", "_baseballbat",
         "_bcards", "bleached", "blog", "_bonehurtingjuice", "_bq", "_brit", "bubblegum", "builders", "bunkers", "butt",
         "cafechan", "caffe", "canada", "_cath", "chori", "choroy", "christian", "christianity", "_christianmeme",
         "cicachan", "civicrs", "ck", "cloveros", "co", "cow", "_cuckquean", "cute", "cyber", "cyoa", "_czech",
         "_dadtalk", "danpu", "dao101", "degen", "delete", "dempart", "desu", "diaperfags", "diaperfetish", "dir",
         "_dolphin", "_dpfag", "_dpr", "druid", "_e9y", "_eatme", "ebola", "eerie", "egy", "egypt", "_etika", "_eu",
         "_euskotxa", "_exit", "f1", "fa", "_fairy", "fallen", "fast", "faygo", "feet", "femaledomination", "feri",
         "_fightcomms", "film", "flemish", "_floss", "fortnite", "freedomzine", "fukemo", "fumo", "fur", "furry", "g",
         "gamergatehq", "genesis", "_gesu", "_ggis", "girltalk", "greenbreeze", "gts", "_haxxor", "hentai",
         "hentaiclub", "_herm", "_hermetics", "_hgb", "hgg", "_hindu", "hisparefugio", "_hissss", "hnt", "hover",
         "hybrids", "_hydrus", "hypno", "_hypnochan", "icup", "imperium", "in", "ipfs", "ircsecrets", "islam", "ita",
         "_jaooo", "jewess", "_jmaatv", "_joker", "jp", "k", "_kekforceusa", "kemono", "kocsog", "kohlchan",
         "_(komica)", "_komika", "kpop", "lain", "_lego", "leo", "lewd", "lit", "_lol", "loomis", "_loroy", "luddite",
         "magick", "maka", "mde", "_merrychristmas", "_miku", "milf", "_mom", "monster", "_msb", "mtb", "mtt", "mu",
         "_n0thingness", "_nanachi", "natiofr", "nep", "newbrit", "newsplus", "_nobody", "nofap", "_nofur", "_nogatco",
         "nothingness", "ntr", "_nuke8", "_oanda", "_ocb", "_ocult", "_omorashi", "_opmk", "os", "otter", "p",
         "_panconleche", "pdfs", "_peaceofmind", "pen", "philosophy", "_pkmns", "pnd", "pokeporn", "polymath", "pone",
         "projectdcomms", "_pyatibrat", "_qm", "qpatriotresearch", "qresearch", "qrnews", "_rand21", "rec", "rmart",
         "_rusrandom", "rzabczan", "s", "s8s", "_sag", "sapphic", "shousa", "_sikhi", "sip", "sl", "_snowboarding",
         "socpl", "strek", "_subs", "_sve", "t", "tan", "tdt", "_tech9", "_techan", "techbunker", "_tek", "templeos",
         "tenda", "teraha", "_texit", "tf2", "_tg", "_thb", "_thedickshow", "throat", "_tibby", "tikilounge", "tkr",
         "_tr55", "_trashcollector", "truthlegion", "tulpamancers", "turul", "tutturu", "tv", "u", "_uaco", "_ucla",
         "underground", "_usersunion", "v", "vichan", "_vietkong", "vietnam", "vore", "vr", "_warposting", "wdsc",
         "webm", "wg", "_wga", "wikieat", "wis", "wmafsex", "_workrelated", "_wqt", "wx", "x", "_xivl", "_xtian",
         "_zoomerright", "zundel", "0", "55sync", "abdl", "alleycat", "_arisu", "_arisubunker", "_arp", "_bane",
         "_bimbohypnosis", "_bluemoon", "bmn", "brains", "cats", "_chance", "clang", "comfy", "_critters", "_cursed",
         "_cvine", "_cze", "d", "dcaco", "_demonp", "_dnmd", "doomer", "doot", "elitabla", "_empanada", "erp",
         "_falseflags", "fashionplus", "_fata", "femdom", "fit", "_flg", "_fr8chan", "futyitorna", "garrett",
         "_giantesshentai", "hentaiporn", "_hmfr", "hooliedayz", "hsp", "_hujszon", "_iep", "just", "k46", "_kind",
         "_kiwc", "kukichan", "_lacajita", "_legos", "_lgd", "liveanarchy", "_luciddreaming", "m", "_mapp", "mental",
         "_mets", "_milhis", "monarchy", "_myon", "newhomosuck", "newsci", "_nine", "_oes", "_onepiece", "_other369",
         "_otomad", "_penguware", "psyid", "qresearch2gen", "rule34", "_satorare", "sonyeon", "split", "_sunflower",
         "_tae", "test", "_tft", "tftg", "toy", "trap", "_vein", "_virtualreality", "vivian", "voros", "wbr", "_weird",
         "wooo", "yuuka", "fringe", "random", "cuteboys", "tech", "_internatiomall", "interracial", "liberty", "htg",
         "mai", "komica", "cutebois", "argentina", "r", "tf", "draftnote", "abcu", "_k117", "britfeel", "liberty",
         "htg", "mai", "komica", "cutebois", "argentina", "r", "tf", "draftnote", "abcu", "_k117", "britfeel", "y",
         "an", "francofil", "portal", "_royalhawk", "_vdm", "_bullmask", "imouto", "tripfriend", "arepa", "rwby", "sw",
         "y", "an", "francofil", "portal", "_royalhawk", "_vdm", "_bullmask", "imouto", "tripfriend", "arepa", "rwby",
         "sw", "magali", "hikki", "biz", "eris", "india", "mg", "magali", "hikki", "biz", "eris", "india", "mg", "out",
         "_infinity", "tifa", "_muslim", "out", "_infinity", "tifa", "_muslim", "slackware", "archivo", "_flatearth",
         "_yaoi", "_boombox", "_wdp", "thedonald", "libertedexpression", "_khyber", "jsr", "slackware", "archivo",
         "_flatearth", "_yaoi", "_boombox", "_wdp", "thedonald", "libertedexpression", "_khyber", "jsr", "fso",
         "wumpawhip", "_buddhismhotline", "indochinaexpats", "_ett", "_redbar", "_skyline350gt", "_asc", "bazafx",
         "bestkorea", "covid19", "_sokra", "_bowsu", "_qpatriotsunited", "_verzet", "_wlctint", "_cultstate", "_melody",
         "_vedic", "yhvh", "1cok", "_astropolis", "fso", "wumpawhip", "_buddhismhotline", "indochinaexpats", "_ett",
         "_redbar", "_skyline350gt", "_asc", "bazafx", "bestkorea", "covid19", "_sokra", "_bowsu", "_qpatriotsunited",
         "_verzet", "_wlctint", "_cultstate", "_melody", "_vedic", "yhvh", "1cok", "_astropolis", "_earthlibfront",
         "_pardochan", "_stanislawowski", "_thetrump", "yukkuri", "1825kun", "cryptobtc", "_isol", "_knights",
         "language", "_rr34", "_sperg", "_awaken", "_belgium", "_blizzard", "_brain", "buddha", "_dbs",
         "_deestevensvoice4you", "_f4net", "_fuckuchina", "_gbtv", "hairygirls", "_hallaca", "_homeowner", "indo",
         "_jersey", "_jigglypuff", "_lbt", "_madh4ckrs", "_medcorp", "_miamichan", "mrsfrisby", "_mulatto", "_mupro",
         "_nhoodlink", "_p5porn", "_patriotrevolution", "_peko", "_projectobject", "_prop", "pups", "_qanonspain",
         "_qcastellano", "_earthlibfront", "_pardochan", "_stanislawowski", "_thetrump", "yukkuri", "1825kun",
         "cryptobtc", "_isol", "_knights", "language", "_rr34", "_sperg", "_awaken", "_belgium", "_blizzard", "_brain",
         "buddha", "_dbs", "_deestevensvoice4you", "_f4net", "_fuckuchina", "_gbtv", "hairygirls", "_hallaca",
         "_homeowner", "indo", "_jersey", "_jigglypuff", "_lbt", "_madh4ckrs", "_medcorp", "_miamichan", "mrsfrisby",
         "_mulatto", "_mupro", "_nhoodlink", "_p5porn", "_patriotrevolution", "_peko", "_projectobject", "_prop",
         "pups", "_qanonspain", "_qcastellano", "qsocial", "_resist", "_revolu", "_skemt", "_sketheory", "_spaceforce",
         "_surro", "_thehand", "_transit", "_vitaecryptocurrency", "qsocial", "_resist", "_revolu", "_skemt",
         "_sketheory", "_spaceforce", "_surro", "_thehand", "_transit", "_vitaecryptocurrency", "midnightriders",
         "tingles", "1cc", "prog", "ytc", "arcagayghetto", "prog", "ytc", "arcagayghetto", "2hu", "o", "warroom", "2hu",
         "o", "warroom", "ebon", "xiaomicha", "ebon", "xiaomicha", "gnosticwarfare", "moldnet", "zenczan", "cosplay",
         "otakus", "nohup", "frenzone", "8dixie", "hqa", "pundit", "vrgg", "uf0", "malaysia", "gnosticwarfare",
         "moldnet", "zenczan", "cosplay", "otakus", "nohup", "frenzone", "8dixie", "hqa", "pundit", "vrgg", "uf0",
         "malaysia", "instruments", "unlightopen", "pso2g", "jozsicsan", "komijoke", "bmsgeu", "92k", "komicaz", "pcal",
         "accent", "wethepatriots", "porussia", "1a", "tarhana", "bigwomen", "maths", "instruments", "unlightopen",
         "pso2g", "jozsicsan", "komijoke", "bmsgeu", "92k", "komicaz", "pcal", "accent", "wethepatriots", "porussia",
         "1a", "tarhana", "bigwomen", "maths", "coffeetalk", "arcader", "kingcrimson", "moonlight", "trkey", "whogen",
         "xivlgr", "amichan", "gendercritical", "inflg", "komicalol", "capcom", "coser", "cud", "feedism", "grc",
         "reimuchan", "stalker2", "2020istheyear", "carib", "jumpchen", "mishmash", "qbl", "sakurachan", "satsukichan",
         "taodick", "aes", "gacha", "nfl2", "redlands", "traditionalcatholics", "tsiou", "airsoft2", "animation",
         "cafardchan", "chrstdis", "coffeetalk", "arcader", "kingcrimson", "moonlight", "trkey", "whogen", "xivlgr",
         "amichan", "gendercritical", "inflg", "komicalol", "capcom", "coser", "cud", "feedism", "grc", "reimuchan",
         "stalker2", "2020istheyear", "carib", "jumpchen", "mishmash", "qbl", "sakurachan", "satsukichan", "taodick",
         "aes", "gacha", "nfl2", "redlands", "traditionalcatholics", "tsiou", "airsoft2", "animation", "cafardchan",
         "chrstdis", "komicamc", "marista", "neetpride", "numis", "progmusic", "retrogaminggifs", "warcraft2004",
         "komicamc", "marista", "neetpride", "numis", "progmusic", "retrogaminggifs", "warcraft2004"),
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
    ),
    "9chan": JsonInfinityNextChanHelper(
        38,
        "https://9chan.tw/",
        "https://9chan.tw/",
        "/thread/",
        "",
        ("nido", "b", "bestpol", "baaa2", "leftcel", "furry", "9", "magalichan", "voat", "tech", "aryan", "egoism",
         "xxx", "norules", "islam", "follaburra", "left", "choroy", "libertarian", "pepinochan", "trannyhate", "chao",
         "cow2", "asmr", "drug", "baaa", "monarchia", "mlpol", "fallen", "tuetuechan", "huaren", "selfimprovement",
         "int", "pdfs", "femdom", "ifunny", "sneedkino", "cueva", "test", "solv", "ckva", "lovelive", "gbtv",
         "bleached", "mu", "starwars", "oldnorse", "incel", "jauria", "meta", "nido", "b", "bestpol", "baaa2",
         "leftcel", "furry", "9", "magalichan", "voat", "tech", "aryan", "egoism", "xxx", "norules", "islam",
         "follaburra", "left", "choroy", "libertarian", "pepinochan", "trannyhate", "chao", "cow2", "asmr", "drug",
         "baaa", "monarchia", "mlpol", "fallen", "tuetuechan", "huaren", "selfimprovement", "int", "pdfs", "femdom",
         "ifunny", "sneedkino", "cueva", "test", "solv", "ckva", "lovelive", "gbtv", "bleached", "mu", "starwars",
         "oldnorse", "incel", "jauria", "meta", "gunt", "civu", "videogames", "ancapgenc", "55san", "chaos",
         "christian", "intl", "alreadythere", "josh", "juantocades", "kpop", "cyoa", "lole", "nagasakiorg", "health",
         "pol2", "collapse", "suicide", "fscchan", "chun", "spee", "bee2", "eroge", "newhalf", "mamertochan", "syspace",
         "bitc0in", "jwgirls", "pink", "bosnia", "beauty", "bastet", "wealth", "csspol", "manada", "warwebms", "wrass",
         "4chanark", "coalfax", "tulpa", "esneines", "garrettandeerie", "tlnprd", "spam", "grand", "55chan", "butopia",
         "bbbb", "harem", "nippon", "loroy", "agdg", "lilium", "ireland", "greatbritain", "voxxe", "karaite",
         "initiate", "nodelete", "toon", "guro", "news", "oppai", "nationalanarchism", "ixit", "roblox", "autism",
         "technology", "bustin", "argentina", "waifu", "money", "newzealand", "jewish", "schiz", "delogged",
         "sonicporn", "guns", "gaychan", "bitwave", "ancap", "civcraft", "imps", "rule34", "retards", "food", "occult",
         "baphomet", "fursuits", "bread", "czsk", "toys", "tacos", "philosophy", "lain", "accel", "leftypol", "neutg",
         "freezone", "musiczone", "medprim", "sonic", "metokur", "jewishniggers9", "anonclub", "miku", "hell",
         "cuteanimegirls", "italia", "bmw", "2drandom", "hentai", "delicious", "entropy", "esoteric", "hack",
         "milliondollarextreme", "antiporn", "emugen", "schizo", "arch", "craft", "antiroot", "fatchan", "trotsky",
         "boris", "pape", "loli", "virgins", "discord", "cuteboys", "lgbq", "shota", "gayporn", "prep", "thule",
         "mental", "scfl", "weeb", "corxea", "loomis", "murderhole", "9tox", "reddit", "europe", "lounge", "image",
         "fascist", "heidi", "j41d3n4n1m4710n5", "onion", "thedickshow", "cute", "hgame", "bovines", "commando",
         "interracial", "schattenkrieg", "foid", "friends", "gurochanlit", "1984", "fatpeoplehate", "hispachan",
         "tuy360", "northwest", "instruments", "1c7k", "vent", "japan", "bantb", "xtian", "tomboy", "bitcoin",
         "bizness", "newpol", "online", "wldm", "pettanko", "qanon", "radfem", "anime", "lift", "cuckime", "missouri",
         "afrochan", "share", "r9001", "ttrpg", "france", "prueba", "warhammer", "text", "enjambre", "bandada",
         "privateparts", "mega", "pen2", "hurt", "jorship", "fatgirls", "ecsy", "redbar", "agatha2", "agatha", "indie",
         "nano", "israel", "trap", "doomer", "girls", "intcraft", "perv", "onlypol", "book", "sanctos", "brasil",
         "oats", "avnol", "trapshota", "thadhs2", "nemunemu", "andes", "terrydavis", "krautchan", "fursecute", "bugs",
         "rdog", "leftnudes", "42069", "furponyweeb", "shrekchan", "shitpostbot", "tenmagab", "newsplus", "bdsm",
         "fren", "seed", "video", "dontknow", "states", "death", "draw", "scp173", "hechoparatestear", "coon", "jazz",
         "homestuck", "worksafegif", "leveloneb", "nodelete2", "cyber", "null", "guessinggames", "fringe",
         "vexillology", "kotatx", "nurd", "nimbusters", "vfur", "startrek", "monster", "mokole", "banter", "mamono",
         "russianskill9chan", "hats", "liberia", "cuckhunt", "lolicon", "imas", "gout", "eceleb", "alaska", "madoka",
         "fuckjannies", "random", "midpol", "9gag", "nigger", "nsgsig", "libpol", "crypto", "hypno", "product", "ketsu",
         "therightstuff", "cons", "digiart", "diochan", "matriarchy", "scifi", "irlnsoc", "chess", "markwiens", "brap",
         "deletethistestboard", "toho", "moonman", "concordia", "bee4", "vcollins", "tjwa", "nederland", "lotr",
         "solar", "comicsgate", "bisdak", "3dprint", "arda", "goodvibes", "bane", "awoo", "digimon", "blacked", "bike",
         "sudpol", "gore", "mecha", "mettaton", "minions", "roze", "ytp2004", "cutefunny", "hisparefugio2", "poopol",
         "normiecontainment", "bogdanoff", "wh40k", "ohio", "meow", "peppep", "drugs", "claw", "christianxpol", "vidya",
         "canpol", "otter", "janny", "heem", "nook", "streamers", "leaf", "hitler", "neovagina", "dprk", "zoopals",
         "xpol", "radio", "catholic", "kiwi", "rekt", "testclover", "ambient", "urbex", "hackfrauds", "2b2t", "xeraph",
         "sergal", "animu", "poop", "safespace", "auspol", "swbunker", "jews", "oregon", "lithuania", "troon", "meme",
         "neet", "kube", "pony", "bans", "jrpg", "hoshikawamafuyu", "rboard", "feet", "politics", "support", "swag",
         "dhsmk2", "weed", "intll", "pokemon", "ecchi", "poli", "hiki", "cuckold", "23213", "ethots", "malware",
         "happening", "neets", "piss", "trump", "joshua", "gifs", "bitch", "9chan", "freech", "neovag", "shit", "edgy",
         "milsperg", "genesis", "4chan", "niggerology", "ratchet", "mugen", "drama", "themes", "animus", "programming",
         "lgbtq", "gurps", "baph", "kind", "commiecat", "poem", "wooo", "cold", "stonks", "tiktok", "kino", "touhou",
         "4xgsg", "frogposting", "yiff", "retw", "wikieat", "manifesto", "neoxen", "hate", "tooter", "wall", "bnwo",
         "lenny", "againsthateboards", "aust", "rwby", "alcohol", "fitlit", "sips", "fedpost", "erpd", "science",
         "rbanter", "venezuela", "consoomer", "1776", "research", "thedonald", "hga2", "testing", "gondola", "drwho",
         "tropic", "rustchan", "mlpp", "vector", "ausneets", "civrealms", "cloth", "comics", "grug", "valve", "simp",
         "ipv6", "rustlang", "lulz", "niggers", "wagie", "cats", "lief", "poke", "pinball", "hist", "intro", "econ",
         "wsgif", "anthro", "corona", "sneed", "dolphin", "para", "julay", "rage", "rust", "abby", "obscuremedia",
         "bqoh", "maga", "9pol", "gamedev", "bible", "nshg", "nite", "9chansupport", "centristpol", "iceposeidon2",
         "scientology", "bunny", "wiki", "cuck", "communism", "bbbc", "popbob", "drater", "tds2", "trans", "jenkem",
         "history", "incels", "smash", "movienight", "pone2", "fash", "pontypandy", "cheat", "photosofjoshuaconnermoon",
         "testboardborad", "yhwh", "murec", "anarcho", "vaporwave", "hypnosis", "green", "taqueria", "s9chs", "grza",
         "testboard", "vd20", "feds", "deep", "archive", "webm", "monkeynoises", "spooky", "raid", "indy",
         "bigtittyslotmachine", "egy", "spacewestern", "videogamegeneral", "hikikomori", "fuckmark", "bose", "fuzhou",
         "print", "panela", "testingoof", "lietuva", "brigade", "cringepol", "snow", "endchan", "waitplz", "vore",
         "sanic", "ranrol", "buttplug", "traditionalgames", "scurv", "shia", "wota", "yugi", "transphobia",
         "soyjakparty", "italy", "atheism", "halal", "kjvbestbible", "market", "fapioh", "en3ma12345m9", "fatego",
         "feedprintersfilament", "cows", "illitterate", "inflation", "unreal", "television", "australia", "ozihcs",
         "soysoy", "cozy", "choroy1111", "fpsg", "nonsensz", "bitte", "discords", "zoomerright", "meadhall",
         "niggersgay", "gdpspawn", "roman", "terf", "buddhist", "atheistpol", "sonicporngeneral", "buddhism", "trihard",
         "pyro", "suggestion", "aaaaaaaaaaaaaaaaaaaa", "emoff", "among", "1488", "bulkcheapammo", "spacechan", "wasp",
         "scat", "witchhouse", "christianpol", "christianity", "obmedia", "darksydephil", "privacy", "operate", "long",
         "leftistpol", "christianidentity", "hnhc", "lawb", "memes", "buddha", "brchan", "truecrime", "meth", "blog",
         "opieandanthony", "help", "mexicali", "natsoc", "cuteboy", "1ccccccccccc", "siberia", "vice", "anarkism",
         "cooking", "photo", "tobacco", "stim", "rand21", "hooch", "christ", "patch", "invaderwatch", "retro", "alogod",
         "cocaine", "deutsch", "streamer", "shrek", "nootropics", "rant", "monarchy", "lbrtn", "arepa", "piripum",
         "dogola", "animalcrossing", "devontracey", "bqoa", "vapor", "kush", "lolnada", "autismawareness",
         "politicallyincorrect", "hockey", "randb", "traps", "vichan", "ircsecrets", "bosartest111111", "chib",
         "testing1234fake", "mdma", "virgo", "homo", "scum", "anal", "gamerhatehq", "vagina", "dump", "advert",
         "jueggin", "kike", "type", "robot", "goodguys", "ween", "bankfraudaccountloading", "vhsch"),
    ),
}
