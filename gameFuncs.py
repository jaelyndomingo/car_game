from pygame import *

# code borrowed from : @josmiley / Luke spywoker
def roundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)


def text_objects(text, font):
    black = (0, 0, 0)
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(surface, msg, x, y, w, h, ic, ac):

    """
    button(msg, x, y, w, h, ic, ac)

    surface : destination
    msg     : button text
    x       : top left x-coordinate of button box
    y       : top left y-coordinate of button box
    w       : button width
    h       : button height
    ic      : inactive color (mouse not hovering)
    ac      : active color (mouse hovering)
    """

    m = mouse.get_pos()

    if x+w > m[0] > x and y+h > m[1] > y:  # mouse hover over start
        roundedRect(surface, (x,y,w,h), ac, 0.5)
    else:
        roundedRect(surface, (x,y,w,h), ic, 0.5)

    small_text = font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, small_text)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    surface.blit(textSurf, textRect)