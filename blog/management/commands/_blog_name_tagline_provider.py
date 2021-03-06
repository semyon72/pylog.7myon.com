# Project: blog_7myon_com
# Package: 
# Filename: _blog_name_tagline_provider.py
# Generated: 2021 Jan 17 at 19:51 
# Description of <_blog_name_tagline_provider>
#
# @author Semyon Mamonov <semyon.mamonov@gmail.com>

import re

resource = r'''Just Do It. (Nike)
Real leather crafted the forgotten way. (Hidesign)
Shave time. Shave money. (Dollar Shave Club)
Melt’s in your mouth, not in your hands. (M&M)
It’s more than good, it’s great. (Frosted Flakes)
A diamond is forever. (De Beers)
With a name like Smuckers, it has to be good. (Smuckers)
Cold as the rockies. (Coors)
Quality never goes out of style. (Levi’s)
Think big. (Imax)
It keeps going… and going… and going. (Energizer)
Refreshes the parts other beers cannot reach. (Heineken)
Can you hear me now? (Verizon) 
Obey your thirst. (Sprite)
The uncola. (7 Up)
Eat fresh. (Subway)
Capitalist tool. (Forbes)
Say it with flowers. (FTD)
Trix are for kids. (Trix Cereal)
Be all you can be. (U.S. Army)
Love is in the air. (Southwest Airlines)
A mind is a terrible thing to waste. (UNCF)
Let your fingers do the walking. (Yellow Pages)
Tastes so good cats ask for it by name. (Meow Mix)
When it absolutely, positively has to be there overnight. (FedEx)
So easy a caveman can do it. (Geico)
Got milk? (California Milk Processing Board)
The breakfast of champions. (Wheaties)
The Citi never sleeps. (Citibank)
Where’s the beef? (Wendy’s)
Designed for driving pleasure. (BMW) 
The quicker picker-upper. (Bounty)
Make believe. (Sony)
Redbull gives you wings. (Redbull)
Betcha can’t eat just one. (Lays)
Taste the rainbow. (Skittles)
We deliver. (USPS)
Think Small. (Volkswagen)
Have a Coke. (Coke)
I’m lovin’ it. (McDonalds)
When you care enough to send the very best. (Hallmark)
All the news that’s fit to print. (New York Times)
Nothing runs like a Deere. (John Deere)
You give us 22 minutes, we’ll give you the world. (1010 Wins)
Imagination at work. (General Electric)
Like a good neighbor, state farm is there. (State Farm)
Maybe she was born with it. Maybe it’s Maybelline. (Maybelline)
Hand-built by robots. (Fiat Strada)
Good to the last drop. (Maxwell House)
That was easy. (Staples)
Pardon me, do you have any Grey Poupon? (Grey Poupon)
Snap! Crackle! Pop! (Rice Krispies)
Leave the driving to us. (Grey Hound)
I think, therefore IBM. (IBM)
Let Hertz put you in the driver’s seat. (Hertz)
We try harder. (Avis)
Finger lickin’ good. (KFC)
Every kiss begins with Kay. (Kay Jewelers)
We’ll leave a light on for you. (Motel 6)
This is your brain on drugs. (Drugs Free America)
America runs on Dunkin’. (Dunkin’ Donuts)
Let’s go places. (Toyota)
The happiest place on Earth. (Disney Land)
Think outside the bun. (Taco Bell)
You’re in good hands. (Allstate)
Ask the man who owns one. (Packard)
Belong anywhere. (AirBnb)
Tastes great, less filling. (Miller Lite)
Impossible is nothing. (Adidas)
I can’t believe I ate the whole thing. (Alka Seltzer)
Stronger than dirt. (Ajax)
The snack that smiles back. (Goldfish)
Gotta Catch ‘em all! (Pokemon)
Go further. (Ford)
Eat more Chikin. (Chick-fil-a)
Democracy dies in darkness. (Washington Post)
What happens here, stays here. (Las Vegas)
'''


def blog_name_tagline_generator():
    for i in re.finditer(r'^(.+)?\s+\((.+)?\).*$', resource, re.MULTILINE):
        yield i.group(1, 2)