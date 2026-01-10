from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings into one string using length-prefixing.

        Format per string: "<length>#<string>"
        Example: ["hi", "world"] -> "2#hi5#world"

        Why this works:
        - We store the length first, so strings can contain ANY characters (including '#')
          without breaking decoding.
        """
        encoded = ""
        for s in strs:
            # Prefix each string with its length and a delimiter '#'
            # so decoding knows exactly how many chars to read next.
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decode a single encoded string back into the original list of strings.

        We scan left-to-right:
        1) Read digits until '#': that's the length L
        2) Read the next L characters: that's the string
        3) Repeat until we reach the end
        """
        decoded = []
        i = 0  # pointer to where the next length starts

        while i < len(s):
            j = i  # pointer used to find the '#'

            # Move j until we hit the delimiter '#'
            # Everything from s[i:j] is the length (as text).
            while s[j] != "#":
                j += 1

            length = int(s[i:j])  # convert length substring to an integer
            start = j + 1         # first character of the actual string
            end = start + length  # end boundary (exclusive)

            # Extract the string of known length and store it
            decoded.append(s[start:end])

            # Jump i to the next length prefix (right after the extracted string)
            i = end

        return decoded
