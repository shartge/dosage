# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre


_imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
_stripPattern = r'([^"]*/d/\d{8}\.html)'
_prevSearch = (
    compile(tagre("link", "href", _stripPattern, before="prev")),
    compile(tagre("a", "href", _stripPattern, after="prev")),
    compile(tagre("a", "href", _stripPattern) + tagre("img", "id", r"previous_day1")),
)

def add(name, url, description):
    classname = 'KeenSpot_%s' % name
    if '/d/' in url:
        stripUrl = url.split('/d/')[0] + '/d/%s.html'
    else:
        stripUrl = url + 'd/%s.html'

    globals()[classname] = make_scraper(classname,
        name='KeenSpot/' + name,
        url=url,
        description=description,
        stripUrl=stripUrl,
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: yyyymmdd',
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('27TwentySeven', 'http://twenty-seven.keenspot.com/', "Hendrix, Cobain, Joplin, Morrison: all belong to the '27 Club,' which admits only the most brilliant musicians...and kills them dead in their 27th year. Will Garland is a famous rock guitarist, secretly unable to play for months due to a neurological disorder afflicting his left hand. He's also 27! Can he make it to 28?")
add('Adventurers', 'http://adventurers.keenspot.com/', "What do a sword-wielding hero, a deeply cynical mage, a complaining theif, a robot spy, a honourable ninja, an obsessed gunslinger, a useless bard, an equally useless cute thing, and a white mage have in common? They're main characters in ADVENTURERS!, for one.")
add('AntiheroForHire', 'http://antihero.keenspot.com/', "Insane supervillains, cryptic madmen, giant monsters, and criminals with high-tech equipment? No problem! It's all in a night's work for Shadehawk, Antihero for Hire. Works on contingency.")
add('BanzaiGirl', 'http://banzaigirl.keenspot.com/', '"Banzai Girl" Jinky Coronado is a popular schoolgirl about to have her big 18th birthday party, when her life gets turned upside-down. Her horrific nightmares literally invade our reality... and those same nightmares may be the key to saving the world!')
add('Barker', 'http://barkercomic.keenspot.com/', 'The story of a boy and his dog.')
add('Buzzboy', 'http://buzzboy.keenspot.com/', "Buzzboy is the world's coolest super sidekick, a cheeseburger-chomping, pop culture-quoting dynamo! But what happens when his mentor, Captain Ultra, and all the top adult superheroes disappear, and Buzzboy and friends are left to save a world where sidekicks rule?")
add('ChoppingBlock', 'http://choppingblock.keenspot.com/', "Y'know how sometimes you hear the voice of your dead mother in your head commanding you to murder sorority girls with a chainsaw and keep their eyeballs in a big jar of formaldehyde? Don't you hate that? I mean, does she have ANY IDEA how hard it is to get your hands on THAT MUCH formaldehyde? Sheesh.")
add('EverythingJake', 'http://everythingjake.keenspot.com/', 'Everything Jake is not just a pun, it\xc2\x92s the story of Jake Bruno, college freshman. It\xc2\x92s chock full of assorted funniness about life, the universe, and everything.')
add('FallOutToyWorks', 'http://fallouttoyworks.keenspot.com/', 'The newly-produced android named Tiffany becomes the greatest passion and potential destruction of a brilliant robot-maker. Inspired by the ideas and lyrics of FALL OUT BOY.')
add('FriarAndBrimstone', 'http://friarandbrimstone.keenspot.com/', '"I\'m gonna summon a demon!"')
add('GeneCatlow', 'http://genecatlow.keenspot.com/', 'A comic that centers on a world populated by both anthropomorphic animals and humans, who have (1) gotten along none too well through the history of their world, and (2) recently had it shown to them in no uncertain terms that they share a common ancestor, responsible for all intellgent life.')
add('GodMode', 'http://godmode.keenspot.com/', "Once upon a time, a teenager created a popular video game cheat code website that was inexplicably bought by a billion-dollar corporation and turned into the ultimate gaming portal. Today, she's all grown up and overseeing the GOD MODE empire with an iron fist and a smoker's cough.")
add('GreenWake', 'http://greenwake.keenspot.com/', 'In the forgotten town of Green Wake, a string of grisly mutilations leads Morley Mack on the trail of a young woman named Ariel, who is the prime suspect. But when a stranger with startling connections to Ariel arrives under mysterious circumstances, Morley unravels a dark plot...')
add('HeadTrip', 'http://headtrip.keenspot.com/', "We're the good kind of crazy, we swear.")
add('JadeWarriors', 'http://jadewarriors.keenspot.com/', 'Angel Sorayama was imbued with the power of a "Deathkiss" as part of a cult of female assassins fostered by the Yakuza for its own ends. When she dared to escape this life, the hunter became the hunted!')
add('Landis', 'http://landis.keenspot.com/', 'The fantastic adventures of an immortal warrior woman searching for the lost hammer of Thor.')
add('MakeshiftMiracle', 'http://makeshiftmiracle.keenspot.com/', 'Colby Reynolds searches for meaning in the world around him and discovers a place where dreams can come true, if he\xc2\x92s willing to pay the price.')
add('Marksmen', 'http://marksmen.keenspot.com/', "Drake McCoy, an expert marksman, defends the future city of New San Diego from the numerous threats in the wasteland outside its walls. But when a powerful army aims to steal the city's energy technology, even Drake's skills may not be enough to fend off the siege.")
add('MarryMe', 'http://marryme.keenspot.com/', 'A romantic comedy graphic novel about a pop star, frustrated with her love life, who marries a random fan holding a \xc2\x93MARRY ME\xc2\x94 sign at one of her concerts.')
add('MedusasDaughter', 'http://medusasdaughter.keenspot.com/', 'Fifteen-year-old sideshow freak Maia Volokos, born with writhing ringlets and viperous locks, seeks the dangerous truth about herself and the parents she never knew.')
add('MonsterMassacre', 'http://monstermassacre.keenspot.com/', 'Massive monsters, bad babes, giant guns, carnasaur carnage, creepy creators... what more could you ask for?')
add('Newshounds', 'http://newshounds.keenspot.com/', "KPET is the home to a woman and her fractious (not to say fractured) talking pets, who report today's news as only talking pets can. See politics intertwined with romance, sports intertwined with intrigue, and comedy intertwined with things comedy shouldn't be intertwined with.")
add('NoPinkPonies', 'http://nopinkponies.keenspot.com/', 'Can a girl go to such extreme just so she can get close to the guy she likes? Jess is just such a girl as she opens up a comic shop and hires the guy of her dreams to work for her. Romantic comedy with a dash of whacky hijinks ensues in this comic about a girl and the what she would do for love. Sort of.')
add('OutThere', 'http://outthere.keenspot.com/', 'A neurotic barmaid encounters a mysterious drifter on the road. The intrepid duo finds they have absolutely nothing in common. So, naturally, they become traveling partners. You know, just like in real life.')
add('QUILTBAG', 'http://quiltbag.keenspot.com/', 'Two young college girls begin a journey of self-discovery on a campus that represents the whole spectrum of sexuality, and possibility.')
add('RedSpike', 'http://redspike.keenspot.com/', 'Project Red Spike was successful in creating the ultimate super soldiers. But what happens when those soldiers stop taking orders?')
add('SamuraisBlood', 'http://samuraisblood.keenspot.com/', 'In an era when lineage defined you, three teenagers must make their way through the world hiding their identities in order to find their destinies.')
add('Sharky', 'http://sharky.keenspot.com/', "For '90s kid Patrick Sharky, there's no comic book superhero cooler than the one that shares his last name: SHARKY, the ultimate tough guy. They say you should never meet your heroes... but Patrick may not have a choice in the matter!")
add('Skullkickers', 'http://skullkickers.keenspot.com/', 'Two hard-headed mercenaries kill monsters and cause havoc in their search for money, fame and adventure. Along the way, they\xc2\x92ll gore goblins, smash skeletons, punch plant people and whomp werewolves.')
add('SomethingHappens', 'http://somethinghappens.keenspot.com/', '"Something Happens" is a weekly comic emphasizing surreal sketch humor, as if \'The Far Side\' were filtered through \'Monty Python.\' The only guarantee made is that the comic will live up to the title, especially if you squint.')
add('SoreThumbs', 'http://sorethumbs.keenspot.com/', "After a beautiful TV horror host's show is cancelled, she's forced to move home to Mayflower, New Jersey and interact with her family and old friends.")
add('Striptease', 'http://striptease.keenspot.com/', "It's not just a clever name for a webcomic.... okay, it is. Sex, betrayal, humor, adventure, and comic book pencilling!")
add('Superosity', 'http://superosity.keenspot.com/', "A lovably insane man-child in a cape. A super-intelligent board-shaped creature. An angry teenager yearning for fame. A century-old turtle who is America's hottest non-white movie star. What do you get when you put them all together? SUPEROSITY! Or hilarity, possibly. One of those.")
add('TheFirstDaughter', 'http://thefirstdaughter.keenspot.com/', "Tasha Tasker has discovered that her dad isn't the only member of the First Family with presidential powers.")
add('WICKEDPOWERED', 'http://wickedpowered.keenspot.com/', 'Three beautiful girls from the laser-obsessed future rescue loser Wiley Schlub from his boring life!')
