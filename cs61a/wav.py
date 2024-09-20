from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    """按.wav 文件要求的编码格式 编码值 x
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    """将波形写入 name
    sampler 描述波形的函数 当输入时间时，输出对应时间的波形值(-1 - 1之间)
    name 输出的.wav文件
    seconds 声音的时长
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def trl(frequency, amplitude=0.3):
    """根据 频率 FREQUENCY 振幅 AMPLITUDE 返回描述三角波形的函数"""
    period = frame_rate // frequency 
    def sampler(t):
        saw_wave = t / period - floor(t / period +  0.5)
        trl_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * trl_wave
    return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    """根据波形函数F 返回一个只在START到END区间有波形的函数
    start 起始时间 秒
    fade 淡入淡出
    """
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave):
    c, e = trl(octave * c_freq), trl(octave * e_freq)
    g, low_g = trl(octave * g_freq), trl(octave * g_freq / 2)
    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song
    
# play(mario_at(1/2))
play(both(mario_at(1), mario_at(1/2)))
