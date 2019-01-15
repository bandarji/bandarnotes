>>> s = 'How might I make alternating caps in python?'
>>> ''.join([l.upper() if i % 2 != 0 else l for i, l in enumerate(s)])
'HOw mIgHt I mAkE AlTeRnAtInG CaPs iN PyThOn?'
