import React from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { useToast } from '@/hooks/use-toast';
import { Textarea } from '@/components/ui/textarea';
import Confetti from 'react-confetti';

interface GameLevelProps {
  level: number;
  code: string;
  solution: string;
  hint: string;
  onComplete: () => void;
  theme: {
    primaryColor: string;
    secondaryColor: string;
    glowEffect: string;
    borderEffect: string;
    textGradient: string;
    cardBg: string;
    animation: string;
  };
}

const GameLevel: React.FC<GameLevelProps> = ({ 
  level, 
  code, 
  solution, 
  hint, 
  onComplete,
  theme 
}) => {
  const [userCode, setUserCode] = React.useState(code);
  const [showHint, setShowHint] = React.useState(false);
  const [showConfetti, setShowConfetti] = React.useState(false);
  const { toast } = useToast();
  const editorRef = React.useRef<HTMLTextAreaElement>(null);

  React.useEffect(() => {
    setUserCode(code);
    setShowHint(false);
    setShowConfetti(false);
  }, [code, level]);

  const handleCodeChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const value = e.target.value;
    setUserCode(value);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = e.currentTarget.selectionStart;
      const end = e.currentTarget.selectionEnd;
      const newValue = userCode.substring(0, start) + '  ' + userCode.substring(end);
      setUserCode(newValue);
      
      // Set cursor position after tab
      setTimeout(() => {
        if (editorRef.current) {
          editorRef.current.selectionStart = editorRef.current.selectionEnd = start + 2;
        }
      }, 0);
    }
  };

  const checkSolution = () => {
    if (userCode.trim() === solution.trim()) {
      // Show confetti if this is level 3 (final level)
      if (level === 3) {
        setShowConfetti(true);
        // Stop confetti after 5 seconds
        setTimeout(() => setShowConfetti(false), 5000);
      }
      
      toast({
        title: "Level Complete! 🎮",
        description: "Great job! You've fixed the syntax error!",
        className: `font-retro ${theme.textGradient}`,
      });
      onComplete();
    } else {
      toast({
        title: "Try Again! 🔄",
        description: "That's not quite right. Keep trying!",
        variant: "destructive",
        className: "font-retro",
      });
    }
  };

  return (
    <>
      {showConfetti && (
        <Confetti
          width={window.innerWidth}
          height={window.innerHeight}
          recycle={false}
          numberOfPieces={500}
          gravity={0.3}
        />
      )}
      <Card className={`p-4 sm:p-6 border-2 transition-all duration-300 
                     ${theme.cardBg} ${theme.borderEffect} ${theme.glowEffect}`}>
        <h2 className={`text-lg sm:text-xl font-retro mb-4 ${theme.textGradient}`}>
          Level {level}
        </h2>
        <div className="mb-4 relative">
          <div className="relative font-mono rounded-lg overflow-hidden">
            <Textarea
              ref={editorRef}
              value={userCode}
              onChange={handleCodeChange}
              onKeyDown={handleKeyDown}
              className={`w-full min-h-[200px] p-4 
                       font-mono text-base rounded-lg border-2 
                       focus:outline-none focus:ring-1 resize-none scrollbar-thin 
                       transition-all duration-300 bg-[#1a1a1a]
                       ${theme.primaryColor} ${theme.borderEffect}`}
              spellCheck="false"
              style={{
                fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
                lineHeight: '1.5',
                tabSize: '2',
              }}
            />
          </div>
        </div>
        <div className="flex flex-col sm:flex-row justify-between items-center gap-3 sm:gap-4">
          <Button
            onClick={() => setShowHint(!showHint)}
            variant="outline"
            className={`w-full sm:w-auto font-retro text-xs sm:text-sm px-6 py-2
                     hover:bg-opacity-10 transition-all duration-200 
                     ${theme.borderEffect} ${theme.secondaryColor}`}
          >
            {showHint ? "Hide Hint" : "Show Hint"}
          </Button>
          <Button
            onClick={checkSolution}
            className={`w-full sm:w-auto font-retro text-xs sm:text-sm px-6 py-2
                     text-white transition-all duration-200 
                     hover:bg-opacity-90 ${theme.glowEffect}`}
          >
            Submit
          </Button>
        </div>
        {showHint && (
          <div className={`mt-4 p-4 rounded-lg border animate-in slide-in-from-bottom duration-300 
                        transition-all ${theme.borderEffect} ${theme.secondaryColor} bg-opacity-10`}>
            <p className="font-retro text-sm">{hint}</p>
          </div>
        )}
      </Card>
    </>
  );
};

export default GameLevel;